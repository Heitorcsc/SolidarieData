from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime 
from db import init_db, SessionLocal
from models import User, Prontuario
from auth import hash_password, verify_password, is_valid_cnpj
from sqlalchemy import or_ # Importar o 'or_' para a busca

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "uma_chave_secreta_local_mude_em_producao"

# cria DB (apenas no início)
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Rota Index MODIFICADA COM LÓGICA DE BUSCA ---
@app.route("/", methods=["GET"])
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = next(get_db())
    user = db.query(User).filter_by(id=session["user_id"]).first()
    
    if not user:
        session.pop("user_id", None)
        flash("Sua sessão expirou, por favor, faça login novamente.")
        return redirect(url_for("login"))

    # --- LÓGICA DE BUSCA ---
    search_query = request.args.get('search_query', '') # Pega o termo da URL
    
    # Query base
    query_base = db.query(Prontuario).filter_by(owner_id=user.id)
    
    if search_query:
        # Filtra pelo nome do paciente OU pelo telefone, se houver busca
        query_base = query_base.filter(
            or_(
                Prontuario.nome_paciente.ilike(f'%{search_query}%'),
                Prontuario.telefone.ilike(f'%{search_query}%')
            )
        )
        
    # Ordena o resultado final por nome
    prontuarios = query_base.order_by(Prontuario.nome_paciente).all()
    # --- FIM DA LÓGICA DE BUSCA ---
    
    return render_template(
        "index.html", 
        user=user, 
        prontuarios=prontuarios, 
        search_query=search_query # Passa o termo de volta
    )
# --- FIM DA MODIFICAÇÃO ---

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        cnpj = request.form["cnpj"]
        pwd = request.form["password"]
        db = next(get_db())
        user = db.query(User).filter_by(cnpj=cnpj).first()
        if user and verify_password(pwd, user.password_hash):
            session["user_id"] = user.id
            return redirect(url_for("index"))
        flash("CNPJ ou senha inválidos")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Você foi desconectado.")
    return redirect(url_for("login"))
    
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        nome_ong = request.form["nome_ong"]
        email = request.form["email"]
        cnpj = request.form["cnpj"]
        endereco = request.form.get("endereco") 
        area = request.form.get("area_especializacao")
        pwd = request.form["password"]
        confirm_pwd = request.form["confirm_password"]

        if pwd != confirm_pwd:
            flash("As senhas não coincidem. Tente novamente.")
            return redirect(url_for("register"))
        
        if not is_valid_cnpj(cnpj): 
            flash("CNPJ inválido")
            return redirect(url_for("register"))
        
        db = next(get_db())
        
        if db.query(User).filter_by(cnpj=cnpj).first():
            flash("CNPJ já cadastrado")
            return redirect(url_for("register"))
        if db.query(User).filter_by(email=email).first():
            flash("E-mail já cadastrado")
            return redirect(url_for("register"))
        
        novo_usuario = User(
            nome_ong=nome_ong,
            email=email,
            cnpj=cnpj,
            endereco=endereco,
            area_especializacao=area,
            password_hash=hash_password(pwd)
        )
        
        db.add(novo_usuario)
        db.commit()
        flash("Conta criada com sucesso. Faça login.")
        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/prontuario/novo", methods=["GET","POST"])
def criar_prontuario():
    if "user_id" not in session:
        return redirect(url_for("login"))
        
    if request.method == "POST":
        db = next(get_db())
        
        data_nasc = request.form.get("data_nascimento")
        data_nascimento_obj = None
        if data_nasc:
            try:
                data_nascimento_obj = datetime.strptime(data_nasc, '%Y-%m-%d').date()
            except ValueError:
                flash("Data de nascimento inválida. Use o formato AAAA-MM-DD.")
                return render_template("criar_prontuario.html")

        novo_prontuario = Prontuario(
            owner_id=session["user_id"],
            nome_paciente = request.form.get("nome_paciente"),
            idade = request.form.get("idade", type=int),
            endereco_paciente = request.form.get("endereco_paciente"),
            bairro = request.form.get("bairro"),
            cidade = request.form.get("cidade"),
            profissao = request.form.get("profissao"),
            telefone = request.form.get("telefone"),
            convenio = request.form.get("convenio"),
            observacoes_medicas = request.form.get("observacoes_medicas"),
            data_nascimento = data_nascimento_obj,
            tipo_sanguineo = request.form.get("tipo_sanguineo"),
            contato_emergencia_nome = request.form.get("contato_emergencia_nome"),
            contato_emergencia_telefone = request.form.get("contato_emergencia_telefone"),
            tem_seguro = request.form.get("tem_seguro"),
            fumante = request.form.get("fumante"),
            tem_alergia = request.form.get("tem_alergia"),
            alergia_descricao = request.form.get("alergia_descricao"),
            alimento_restricao = request.form.get("alimento_restricao"),
            tem_medicamento = request.form.get("tem_medicamento"),
            medicamento_descricao = request.form.get("medicamento_descricao"),
            condicao_fisica = request.form.get("condicao_fisica")
        )
        
        db.add(novo_prontuario)
        db.commit()
        return redirect(url_for("index"))
        
    return render_template("criar_prontuario.html")

@app.route("/prontuario/ver/<int:prontuario_id>", methods=["GET", "POST"])
def ver_prontuario(prontuario_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = next(get_db())
    
    prontuario = db.query(Prontuario).filter_by(id=prontuario_id, owner_id=session["user_id"]).first()
    
    if not prontuario:
        flash("Prontuário não encontrado.")
        return redirect(url_for("index"))

    if request.method == "POST":
        nova_observacao = request.form.get("nova_observacao")
        if nova_observacao:
            data_hoje = datetime.utcnow().strftime("%d/%m/%Y %H:%M (UTC)")
            texto_antigo = prontuario.observacoes_medicas if prontuario.observacoes_medicas else ""
            prontuario.observacoes_medicas = (
                f"--- (Atualizado em {data_hoje}) ---\n"
                f"{nova_observacao}\n\n"
                f"{texto_antigo}"
            )
            db.commit()
            flash("Observação adicionada com sucesso!")
        
        return redirect(url_for("ver_prontuario", prontuario_id=prontuario.id))

    return render_template("ver_prontuario.html", prontuario=prontuario)

@app.route("/prontuario/delete/<int:prontuario_id>", methods=["POST"])
def delete_prontuario(prontuario_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = next(get_db())
    prontuario = db.query(Prontuario).filter_by(id=prontuario_id, owner_id=session["user_id"]).first()
    if prontuario:
        db.delete(prontuario)
        db.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
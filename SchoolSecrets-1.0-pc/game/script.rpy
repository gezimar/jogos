image camila = im.Scale ("camila.png",540, 960, xoffset =0, yoffset=0)
image camilas = im.Scale ("camila-sumida-PhotoRoom.png",540, 960, xoffset =0, yoffset=0)
image camila_box = im.Scale ("camila_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image marco = im.Scale ("marco.png",540, 960, xoffset =0, yoffset=0)
image marcos = im.Scale ("marco-sumido-PhotoRoom (1).png",540, 960, xoffset =0, yoffset=0)
image marco_box = im.Scale ("marco_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image jacob = im.Scale ("jacob.png",540, 960, xoffset =0, yoffset=0)
image jacobs = im.Scale ("jacob-sumido-PhotoRoom.png",540, 960, xoffset =0, yoffset=0)
image jacob_box = im.Scale ("jacob_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image kaito = im.Scale ("kaito.png",540, 960, xoffset =0, yoffset=0)
image kaitos = im.Scale ("kaito-sumido-PhotoRoom.png",540, 960, xoffset =0, yoffset=0)
image kaito_box = im.Scale ("kaito_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image astrid = im.Scale ("astrid.png",540, 960, xoffset =0, yoffset=0)
image astrids = im.Scale ("astrid-sumida-PhotoRoom.png",540, 960, xoffset =0, yoffset=0)
image astrid_box = im.Scale ("astrid_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image jonathan = im.Scale ("jonathan.png",540, 960, xoffset =0, yoffset=0)
image jonathans = im.Scale ("jonathan-sumido-PhotoRoom.png",540, 960, xoffset =0, yoffset=0)
image jonathan_box = im.Scale ("jonathan_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image player_box = im.Scale ("player_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)
image padrao_box = im.Scale ("padrao_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image regina = im.Scale ("regina.png",540, 960, xoffset =0, yoffset=0)
image reginas = im.Scale ("reginas.png",540, 960, xoffset =0, yoffset=0)
image regina_box = im.Scale ("regina( enfermeira)_dialogue_box.png",1400, 300, xoffset =260, yoffset=0)

image mochila = im.Scale ("mochila kaito.png",120, 120, xoffset =-45, yoffset=-275)
image desenho = im.Scale ("anotações-removebg-preview.png",600, 600, xoffset =0, yoffset=-300)

image mesa1 = im.Scale ("mesa_01.png",1920, 1080, xoffset =0, yoffset=0)
image mesa2 = im.Scale ("mesa_02.png",1920, 1080, xoffset =0, yoffset=0)
image mesa3 = im.Scale ("mesa_03.png",1920, 1080, xoffset =0, yoffset=0)
image ato1 = im.Scale ("ato 01.png",1920, 1080, xoffset =0, yoffset=0)
image ato2 = im.Scale ("ato 02.png",1920, 1080, xoffset =0, yoffset=0)
image ato3 = im.Scale ("ato 03.png",1920, 1080, xoffset =0, yoffset=0)
image ato4 = im.Scale ("ato 04.png",1920, 1080, xoffset =0, yoffset=0)
image escolafora = im.Scale ("escola-fora.png",1920, 1080, xoffset =0, yoffset=0)
image banheiro = im.Scale ("banheiro.png",1920, 1080, xoffset =0, yoffset=0)
image cantina = im.Scale ("cantina.png",1920, 1080, xoffset =0, yoffset=0)
image corredor1 = im.Scale ("corredor 01.png",1920, 1080, xoffset =0, yoffset=0)
image corredor2 = im.Scale ("corredor dos quartos.png",1920, 1080, xoffset =0, yoffset=0)
image corredor3 = im.Scale ("Corredor_vazio.png",1920, 1080, xoffset =0, yoffset=0)
image enfermaria = im.Scale ("enfermaria.png",1920, 1080, xoffset =0, yoffset=0)
image escolafeio = im.Scale ("escola-canto feio.png",1920, 1080, xoffset =0, yoffset=0)
image salavazia = im.Scale ("Sala de Aula.png",1920, 1080, xoffset =0, yoffset=0)
image fundopreto = im.Scale ("fundopreto.png",1920, 1080, xoffset =0, yoffset=0)
image biblioteca = im.Scale ("biblioteca.png",1920, 1080, xoffset =0, yoffset=0)
image banheiroastrid = im.Scale ("banheiro- astrid morta.png",1920, 1080, xoffset =0, yoffset=0)
image quartojacob = im.Scale ("quarto do jacob.png",1920, 1080, xoffset =0, yoffset=0)
image quartocama = im.Scale ("puzzle cama.png",1920, 1080, xoffset =0, yoffset=0)
image telafim = im.Scale ("tela_fim.jpg",1920, 1080, xoffset =0, yoffset=0)
image creditos = im.Scale ("creditos.png",1920, 1080, xoffset =0, yoffset=0)
label start:
    play music "prologo.mp3"
    python:
        Nome = renpy.input("Como se chama o protagonista desta historia?")
    menu: 
        "[Nome] se indentifica como?"

        "Homem":
            jump masculino

        "Mulher":
            jump feminino
label masculino:
    $ genero = "o"
    $ um = "um"
    $ senhor = "senhor"
    $ pronto = "pronto"
    $ e = "e"
    $ guri = "guri"
    $ homem = "homem"
    jump continuar

label feminino:
    $ genero = "a"
    $ um = "uma"
    $ senhor = "senhorita"
    $ pronto = "pronta"
    $ e = "a"
    $ guri = "guria"
    $ homem = "mulher"
    jump continuar
label continuar:
    scene mesa1
    show padrao_box at left
    "{color=#0a0000}Dia 11 de fevereiro e o ano era 1984. Você é [um] detetive estagiári[genero] que está em uma de suas primeiras missões, você está sentad[genero] na sala de espera tomando um café, pensando em um acontecimento trágico que ocorreu recentemente.{/color}"
    "{color=#0a0000}Quando de repente você escuta um homem chamando você.{/color}"
    "{color=#0a0000}[Nome], por favor me acompanhe, seu chefe precisa de você.{/color}"
    "{color=#0a0000}Você imediatamente aceita, até porque precisava trabalhar. Então você entra na sala e seu chefe diz o seguinte:{/color}"
    "{color=#0a0000}Peço perdão pelo incomodo, mas essa tarefa que irei passar para você será algo acima do seu nível atual e consequentemente será algo que fará você subir de cargo.{/color}"
    hide padrao_box

    show player_box at left
    "{color=#0a0000}Não tem problema, O que gostaria que eu fizesse?{/color}"
    hide player_box

    show padrao_box at left
    "{color=#0a0000}Quero que se infiltre na escola João Pedro Filho e descubra para nós quem matou Olivia Mohammed Al-Kudsi.{/color}"
    "{color=#0a0000}Você fica intrigad[genero], aquele evento trágico que estava pensando era justamente relacionado à Olivia. Ela era sua prima, porém era muito próxima de ti.{/color}"
    hide padrao_box

    show player_box at left
    "{color=#0a0000}Está bem senhor, mas eu não tenho certeza que irei conseguir solucionar, até porque eu sou... Estagiári[genero]...{/color}"
    hide player_box
    scene mesa2
    show padrao_box at left
    "{color=#0a0000}Seu chefe ri um pouco e olha para você.{/color}"
    "{color=#0a0000}Por isso que te enviei para esse serviço. É para ser promovid[genero], mas se não quer uma promoção, ok, arrumaremos um serviço mais básico pra você..{/color}"
    "{color=#0a0000}Você pensa bem sobre isso, havia uma hipótese muito forte relacionada a esse caso. Olivia, meses antes dela morrer, estava muito mal mentalmente, parecia extremamente abatida.{/color}"
    "{color=#0a0000}Você havia cogitado que aquilo era suicídio até porque não tinha nenhuma prova que alguém havia matado ela. Mas se alguém houvesse matado ela, você não iria proteger a honra de Olívia.{/color}"
    "{color=#0a0000}Então você decidiu se juntar à missão, não só por promoção mas acima de tudo pela honra de sua prima para que ela pudesse descansar em paz.{/color}"
    hide padrao_box

    show player_box at left
    "{color=#0a0000}Tudo bem, eu aceito me infiltrar nessa escola e desvendar esse caso.{/color}"
    hide player_box
    scene mesa3
    show padrao_box at left
    "{color=#0a0000}O chefe sorriu para você. Após isso mostrou uma lista de suspeitos.{/color}"
    "{color=#0a0000}Aqui estão, para facilitar para [genero] [senhor]. Esses são os suspeitos que temos, são os mais prováveis que tenham assassinado Olívia. Preciso que foque principalmente neles.{/color}"
    '{color=#0a0000}Você reconhecia alguns por menção, o que poderia facilitar. Você estava com a "faca e o queijo" na mão. Agora era o momento em que aquele peso da morte de sua prima poderia ser aliviado. Com apenas duas palavras você iria finalmente conseguir esse feito.{/color}'
    hide padrao_box

    show player_box at left
    "{color=#0a0000}Estou [pronto].{/color}"
    hide player_box

    show padrao_box at left
    "{color=#0a0000}Ótimo, então pode começar. Está liberad[genero] para a missão.{/color}"
    hide padrao_box
    scene ato1 
    " "
    #-------------------------------------------------------------------ATO 1 ---------------------------------------------------------------------------------
    
    scene escolafora
    with pixellate
    play music "Escola-fora ambientação.mp3"
    show player_box at left
    "{color=#0a0000}Finalmente consegui me infiltrar, graças à direção e a coordenação, resolveram colaborar comigo e fazer com que eu conseguisse me passar por estudante.{/color}"
    "{color=#0a0000}De repente vejo um rapaz com uma pose de ordem para mim e parecia um tanto... formal?{/color}"
    hide player_box

    show kaito
    with fade
    show kaito_box at left
    "{color=#0a0000}Bom dia, você deve ser a nova alun[genero], certo? Bem, como o tempo está apertado, poderei apresentar a escola depois. Venha, vou te levar até a sombria...sala de aula.{/color}"
    hide kaito_box

    show player_box at left
    "{color=#0a0000}Sombria?{/color}"
    hide player_box

    show padrao_box at left
    "{color=#0a0000}Kaito me olhou de forma sería e misteriosa.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Há espíritos malignos nessa sala, nos quais apenas eu tenho a habilidade de vê-los.{/color}"
    hide kaito_box

    show player_box at left
    "{color=#0a0000}Esse cara não batia bem da cabeça...{/color}"
    hide player_box

    menu: 
        "Está bem, vamos para a sala. Obrigada pelo aviso.":
            jump irsala

        "Espíritos malignos??? Você parece que vive no mundo da Lua, não sei não hein?":
            jump espiritos
    
label irsala:
    show padrao_box at left
    "{color=#0a0000}Kaito responde com um sorriso convencido{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Oh, de nada, apenas me sinto lisonjeado que não riu do meu talento especial...{/color}"
    hide kaito_box
    
    show padrao_box at left
    "{color=#0a0000}Ele te leva até à sala.{/color}"
    hide padrao_box
    jump continuar1

label espiritos:
    show padrao_box at left
    "{color=#0a0000}Kaito te olha irritado{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}O QUE???? mundo da Lua???? Você está subestimando os espíritos malignos aqui não é?{/color}"
    hide kaito_box

    show padrao_box at left
    "{color=#0a0000}Ele muda a expressão para apreensão.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Agh isso não importa, vamos para a sala logo! Não vou discutir com seres ignorantes...{/color}"
    hide kaito_box
    jump continuar1
label continuar1:
    
    scene salavazia
    play music "Sala de Aula ambientação.mp3"
    with fade
    show kaito at left
    with fade
    show padrao_box at left
    "{color=#0a0000}Kaito olhou para uma garota que estava tentando segurar o riso.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Ah! Esqueci de me apresentar! Sou Kaito e sou o representante de turma dessa sala.{/color}"
    hide kaito_box

    show padrao_box at left
    "{color=#0a0000}A garota então decidiu falar rindo{/color}"
    hide padrao_box
    hide kaito
    show kaitos at left
    show camila at right
    with fade

    show camila_box at left
    "{color=#0a0000}É representante porra nenhuma!{/color}"
    hide camila_box

    show padrao_box at left
    "{color=#0a0000}Ela parecia ser bem sincera e direta, achei engraçada a situação. Vi Kaito se virando para ela e gritando de forma envergonhada e irritada.{/color}"
    hide padrao_box
    hide camila
    show camilas at right
    hide kaitos
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}CALA A BOCA! EU SOU SIM! Está vendo essa estrelinha na minha blusa???  A professora disse que sou um bom exemplo de aluno e me deu essa estrelinha aqui!{/color}"
    hide kaito_box

    show padrao_box at left    
    "{color=#0a0000}Camila olhou com deboche.{/color}"
    hide padrao_box
    hide kaito
    show kaitos at left
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}E...?{/color}"
    hide camila_box
    hide camila
    hide kaitos
    show camilas at right
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}É UM SÍMBOLO DE HONRA!{/color}"
    hide kaito_box
    hide kaito
    hide camilas
    show kaitos at left
    show camila at right
    show padrao_box at left
    "{color=#0a0000}Camila enquanto isso estava rindo de mais.{/color}"
    hide padrao_box

    show camila_box at left
    "{color=#0a0000}Tsk... Vai lá com sua estrelinha do representante e vai mostrar pra verdadeira representante e vê o que ela diz.{/color}"
    hide camila_box
    hide camila
    hide kaitos
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}É isso o que vou fazer!{/color}"
    hide kaito_box
    hide kaito

    show padrao_box at left
    "{color=#0a0000}Ele entrou na sala bem irritado, se sentou em um lugar e ficou lendo um livro.{/color}"
    "{color=#0a0000}Após um tempo, eu tive que me apresentar aos demais alunos.{/color}"
    hide padrao_box

    show player_box at left
    "{color=#0a0000} Meu nome é [Nome], tenho 18 anos e sou [um] alun[genero] transferid[genero] do Bangladesh. Prazer em conhecer vocês, espero que possamos nos dar bem.{/color}"
    hide player_box

    show padrao_box at left
    play sound "ato 1 - player separando fichas na carteira.mp3"
    "{color=#0a0000}Quando me sentei, ainda bem que era no fundo, decidi separar as fichas dos suspeitos e ordená-las corretamente. Fazer algumas anotações que observei sobre Kaito e Camila que estava dentre os suspeitos, até que ouvi dois alunos conversando do meu lado e pareciam estar falando de mim.{/color}"
    "{color=#0a0000}Até que eu ouvi a voz de um deles decidindo ir falar comigo.{/color}"
    hide padrao_box

    show marco at right
    with fade
    show marco_box at left
    "{color=#0a0000}É melhor a gente falar com ess[e] min[genero] aí! Eu acho injusto essa palhaçada de suspeitarem da gente, principalmente de mim! Ah mas eu vou reclamar...{/color}"
    hide marco_box

    show padrao_box at left
    play sound "ato 1 - jacob afinando violão.mp3"
    "{color=#0a0000}O outro garoto parecia estar afinando as cordas de um violão enquanto falava.{/color}"
    hide padrao_box
    
    show jacob at left
    with fade
    hide marco
    show marcos at right
    show jacob_box at left
    "{color=#0a0000}Calma, el[e] é [um] detetive e está apenas fazendo o trabalho del[e].{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show marco_box at left
    stop sound 
    "{color=#0a0000}Isso não importa! Por que justo a gente??? Eu não fiz nada de errado!{/color}"
    hide marco_box
    
    show padrao_box at left
    "{color=#0a0000}O garoto loiro se virou para mim de forma extremamente chateada, respirou fundo e decidiu falar com calma.{/color}"
    hide padrao_box
    
    show marco_box at left
    "{color=#0a0000}Agh, seguinte amig[genero], infelizmente descobrimos que você está nos investigando, mas saiba que eu não tenho nada haver com essa história! Nem eu nem o Jacob! Então vê se para com essa palhaçada, isso tá me deixando preocupado!{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show padrao_box at left
    '{color=#0a0000}O tal do Jacob olhou para Marco com um olhar de "Já deu?"{/color}'
    hide padrao_box
    
    show jacob_box at left
    "{color=#0a0000}Não se preocupe, meu bem, o Marco não é assim toda hora, ele só está um pouco chateado mas Jajá ele melhora.{/color}"
    hide jacob_box
    
    show padrao_box at left
    "{color=#0a0000}Jacob falando sorrindo gentilmente.{/color}"
    hide padrao_box

menu: 
    "Muito obrigad[genero], não há problema com a atitude dele. Eu compreendo perfeitamente.":
        jump tudobem

    "Nossa, ele é assim sempre?":
        jump sempre

label tudobem:

    show padrao_box at left
    "{color=#0a0000}Jacob sorri.{/color}"
    hide padrao_box

    show jacob_box at left
    "{color=#0a0000}Da pra entender mesmo, acho que sou um tanto mais calmo.{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show marco_box at left
    "{color=#0a0000}Hum, ainda bem que ela compreende. E você é tudo menos calmo, pode crer.{/color}"
    hide marco_box
    hide marco
    hide jacobs
    jump continuar2

label sempre:
    hide jacob
    hide marcos
    show jacobs at left
    show marco at right
    show marco_box at left
    "{color=#0a0000}EI!{/color}"
    hide marco_box
    hide jacobs
    show jacob at left
    hide marco
    show marcos at right
    show jacob_box at left
    "{color=#0a0000}Apenas quando pisam no calo dele. Tem vez que até eu perco a paciência.{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    show marco at right
    show marco_box at left
    "{color=#0a0000}Aaah tenha dó né? Pelo amor de Deus, até você tá reclamando de mim rapaz?{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show padrao_box at left
    "{color=#0a0000}Jacob parecia ter se irritado.{/color}"
    hide padrao_box

    show jacob_box at left
    "{color=#0a0000}OOOH! Menos, Marco! Mas que saco!{/color}"
    hide jacob_box
    hide jacob
    hide marcos
    jump continuar2

label continuar2:
    show jacob at left
    show marcos at right
    show jacob_box at left
    "{color=#0a0000}Mas não se preocupe! De qualquer forma, você é [um] detetive incrível e sei que vai conseguir realizar seu trabalho.{/color}"
    hide jacob_box
    hide jacob 
    show jacobs at left
    hide marcos
    show marco at right
    show padrao_box at left

    "{color=#0a0000}Marco falou um pouco mais sério e menos irritado.{/color}"
    hide padrao_box
    
    show marco_box at left
    "{color=#0a0000}É, que seja! A gente vai ter que ajudar [genero] [guri] aí, embora eu não esteja gostando tanto dessa situação. {/color}"
    hide marco_box
    
    show padrao_box at left
    "{color=#0a0000}Parece que ele finalmente deu um sorriso reconfortante.{/color}"
    hide padrao_box
    
    show marco_box at left
    "{color=#0a0000}Venha! Vamos apresentar a escola pra você. E quem sabe a gente quebra um galho apresentando os suspeitos já.{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Marco, tem uns aí que a gente nem fala tanto, uns são até meio...{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show marco_box at left
    "{color=#0a0000}Babacas? Ah sim, o enjoadão do Jonathan. Ele é um merda mesmo! Mas de qualquer maneira el[e] vai ter que se arriscar e conversar com ele, a gente vai ter que estar do lado del[e].{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}É, você tem razão...{/color}"
    hide jacob_box

    show padrao_box at left
    "{color=#0a0000}Eu já comecei a ficar um tanto com um pé atrás sobre esse tal do Jonathan.{/color}"
    hide padrao_box
    
    show player_box at left
    "{color=#0a0000}Jonathan? Ele é tão problemático assim?{/color}"
    hide player_box
    
    show jacob_box at left
    "{color=#0a0000}Terrível. Ele já teve alguns problemas com a polícia inclusive. Ele briga direto na escola, tem até rotina disso. {/color}"
    "{color=#0a0000}A gente tem costume de chamar a sexta - feira de Treta- feira porque o Jonathan costuma brigar muito principalmente nesses dias.{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show padrao_box at left
    "{color=#0a0000}Marco sorriu gentilmente.{/color}"
    hide padrao_box

    show marco_box at left
    "{color=#0a0000}Calma Jacob, não fala tanto, ou você vai deixar [genero] [homem] meio cabreir[genero] e el[e] vai ter medo de falar com ele.{/color}"
    hide marco_box
    
    show player_box at left
    "{color=#0a0000}Na verdade não (falei rindo) Ok, talvez um pouco.{/color}"
    hide player_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}É bom mesmo. (Ele falou rindo){/color}"
    hide jacob_box
    hide jacob
    hide marcos
    scene corredor1
    with fade
    play music "Corredor ambientação.mp3"

    show marco at right
    show jacob at left
    show padrao_box at left
    "{color=#0a0000}Os dois então decidiram me apresentar a escola. Saímos da sala.{/color}"
    hide padrao_box
    hide jacob
    show jacobs at left
    show marco_box at left
    "{color=#0a0000}Aqui é o corredor principal... Ah não liga pras pixações não, esse porra do Jonathan até fez uma aqui ó.{/color}"
    hide marco_box
    
    show player_box at left
    "{color=#0a0000}Pelo jeito vocês amam esse Jonathan hein?{/color}"
    hide player_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Amamos tanto, falamos tanto dele, meu medo é dele descobrir os desenhos feios que a gente faz dele e xinga. A gente iria parar no hospital com certeza.{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show marco_box at left
    "{color=#0a0000}Uma vez quase que ele descobriu.{/color}"
    hide marco_box
    
    show padrao_box at left
    "{color=#0a0000}Marco falou rindo.{/color}"
    "{color=#0a0000}Parecia realmente que esse Jonathan era perigoso como diziam. {/color}"
    hide padrao_box
    hide marco
    hide jacob
    scene corredor3
    with fade
    play music "Corredor ambientação.mp3"

    show marco at left
    show jacobs at right
    show marco_box at left
    "{color=#0a0000}Aqui é a escadaria, onde o Kaito diz que alguém já morreu aqui. Esse é um esquisitão mas ele é bonzinho até de mais, bem inocente também. A Camila gosta de zoar ele mas ela não faz na maldade até onde eu sei.{/color}"
    hide marco_box
    hide Marco
    show marcos at left
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Ah, precisamos mostrar o melhor lugar de todos! O lugar favorito do Kaito, a biblioteca!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Sim, nos siga por favor.{/color}"
    hide marco_box
    hide marco
    hide jacobs
    scene biblioteca
    with fade
    play music "Biblioteca ambientação.mp3"

    show padrao_box at left
    "{color=#0a0000}Eu segui eles até à biblioteca, quando entramos lá, vi uma garota loira que me olhou com um certo desdém.{/color}"
    hide padrao_box at left
    
    show astrid
    with fade
    show astrid_box at left
    "{color=#0a0000}Você deve ser [genero] aluna nov[genero]. Eu sou a Astrid, representante de turma. Agora deixa eu finalizar a tarefa.{/color}"
    hide astrid_box
    hide astrid
    
    show padrao_box at left
    "{color=#0a0000}Ela falou de uma forma grosseira, porém dava pra entender, não era de todo mal.{/color}"
    hide padrao_box

    scene cantina
    with fade
    play music "audio/Cantina ambientação.mp3"

    show marco at left
    show jacob at right
    show padrao_box at left
    "{color=#0a0000}Fomos então para a cantina, onde vi um homem ruivo e bem musculoso extremamente irritado, parecia ter acabado de sair de uma briga.{/color}"
    '{color=#0a0000}Hoje era a tal da "Treta-feira" que o Jacob havia mencionado.{/color}'
    hide padrao_box
    hide jacob
    show jacobs at right
    show padrao_box at left
    "{color=#0a0000}Marco falou no meu ouvido.{/color}"
    hide padrao_box
    
    show marco_box at left
    "{color=#0a0000}Esse é o insuportável do Jo-{/color}"
    hide marco_box
    hide marco
    show marcos at left
    show padrao_box at left
    "{color=#0a0000}Quando Jonathan olhou para nós de forma extremamente irada mas não parecia querer nada.{/color}"
    hide padrao_box

    show jonathan
    with fade
    show jonathan_box at left

    "{color=#0a0000}Oi, você é [genero] gatinh[genero] que é nov[genero] na sala? Eu sou o Jonathan, seguinte, eu vou ali comer meu lanche, depois a gente se fala. Ah, nem sei porque quis fazer amizade com esses dois cabeças de merda! Ah que se dane, tchau!{/color}"
    hide jonathan
    hide jonathan_box
    
    show padrao_box at left
    "{color=#0a0000}Ele falou saindo.{/color}"
    hide padrao_box
    hide marcos
    hide jacobs
    
    scene corredor1
    with fade
    play music "Corredor ambientação.mp3"

    show marco at right
    show jacobs at left
    show marco_box at left
    "{color=#0a0000}Você viu??? Como o Jonathan é imbecil, ainda te cantou, sabia que ele tem namorada? Esse cara não vale nada mesmo.{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}E ainda xingou a gente! Ah mas isso não importa, eu tenho 1,97 de altura, consigo bater nele! Se ele mexer contigo, me avisa.{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show player_box at left
    "{color=#0a0000}Obrigad[genero], mas não sei se vai ser necessário. Bem, de qualquer forma Jonathan está sendo o principal suspeito aqui, e mesmo se ele não for o verdadeiro assassino, ele vai ter que se ver com a justiça de algum jeito.{/color}"
    hide player_box
    
    show padrao_box at left
    "{color=#0a0000}Marco e Jacob riram.{/color}"
    hide padrao_box

    show marco_box at left
    "{color=#0a0000}Bem, foi um prazer conhecer você, [Nome].{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Verdade, vejamos você amanhã!{/color}"
    hide jacob_box

    show padrao_box at left
    "{color=#0a0000}Eles falaram sorrindo e me despedi deles.{/color}"
    # These display lines of dialogue.
    hide jacob
    hide marcos
    hide padrao_box
    scene ato2
    " "
#------------------------------------------------------------ATO 2 --------------------------------------------------------------------------------------
    scene salavazia
    play music "Sala de Aula ambientação.mp3"
    show padrao_box at left
    "{color=#0a0000}Já havia passado 1 semana desde que eu estava infiltrad[genero] na escola e tínhamos voltado do intervalo. Vi Kaito entrando na sala pra pegar o material dele, quando ele olhou para a carteira da sala e não viu a mochila dele. {/color}"
    hide padrao_box
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}[Nome] você viu minha mochila? É que eu preciso entregar a tarefa pra professora porque do nada ela decidiu que era pra entregar agora nessa aula. Ela as vezes me tira do sério.{/color}"
    hide kaito_box

    show player_box at left
    "{color=#0a0000}não vi não... Mas espero que você consiga achar.{/color}"
    hide player_box

    show kaito_box at left
    "{color=#0a0000}Aah que droga... Obrigado!{/color}"
    hide kaito_box
    hide kaito
    show kaito at left
    show player_box at left
    "{color=#0a0000}De nada, Kaito.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Após isso, Kaito procurou e a medida que não encontrava, ele começou a entrar em desespero.{/color}"
    "{color=#0a0000}Kaito então viu Camila entrando na sala e resolveu falar com ela.{/color}"
    hide padrao_box
    hide kaitos
    show kaito at left
    show camilas at right
    show kaito_box at left
    "{color=#0a0000}Oi Camila! Tudo bem?{/color}"
    hide kaito_box

    show padrao_box at left
    "{color=#0a0000}Ele falou mas deu pra perceber um leve toque de irritação no tom da sua voz.{/color}"
    hide padrao_box
    hide kaito
    show kaitos at left
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}Estou bem sim!{/color}"
    hide camila_box
    hide camila
    show camilas at right
    hide kaitos
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}Eu queria saber onde está minha mochila, você viu onde está???{/color}"
    hide kaito_box
    hide kaito
    show kaitos at left
    hide camilas 
    show camila at right
    show camila_box at left
    "{color=#0a0000}Não vi não, meu bem.{/color}"
    hide camila_box
    
    show padrao_box at left
    "{color=#0a0000}Ela falou rindo um pouco.{/color}"
    hide padrao_box
    hide camila
    show camilas at right
    hide kaitos
    show kaito at left
    show padrao_box at left
    "{color=#0a0000}Kaito de repente fechou a cara e falou em um tom mais ríspido.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Você escondeu a minha mochila né? {/color}"
    "{color=#0a0000}DEVOLVE AGORA!{/color}"
    hide kaito_box
    hide kaito
    show kaitos at left
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}Mas eu não escondi mochila de ninguém!{/color}"
    hide camila_box
    
    show padrao_box at left
    "{color=#0a0000}Ela falou entre risos.{/color}"
    hide padrao_box
    hide camila
    show camilas at right
    hide kaitos
    show kaito at left
    show padrao_box at left
    "{color=#0a0000}Kaito percebeu que ela estava rindo e ficou com uma irritação extremamente aparente.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}DEVOLVE MINHA MOCHILA! ONDE VOCÊ COLOCOU ELA???{/color}"
    hide kaito_box
    hide kaito
    show kaitos at left
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}A mochila não tá comigo, se quiser vai lá procurar, meu anjo.{/color}"
    hide camila_box

    show padrao_box at left
    "{color=#0a0000}Ela falou dando um sorriso de canto.{/color}"
    hide padrao_box
    hide camila
    show camilas at right
    hide kaitos
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}TU VAI VER ESSE ANJINHO VIRAR O CAPETA EM PESSOA SE VOCÊ OUSAR CONTINUAR ME ENCHENDO O SACO, ME DIZ ONDE ESTÁ A MOCHILA!{/color}"
    hide kaito_box
    hide kaito
    show kaitos at left
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}Procura aí...{/color}"
    hide camila_box
    hide camila
    hide kaitos

    show kaito at center
    show padrao_box at left
    "{color=#0a0000}Kaito bateu com o pé no chão e correu pra mim dando um suspiro mas mesmo assim não parecia estar calmo e sim, extremamente ansioso.{/color}"
    hide padrao_box

menu:
    "Não, se vira aí rapaz.":
        jump naoajudar
    "Posso sim.":
        jump ajudar
label naoajudar:
    show padrao_box at left
    "{color=#0a0000}Kaito me olhou furioso e chateado ao mesmo tempo.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Tá bom então, [Nome]! É assim né??? Você é igual a esses idiotas então, né? Ficam me zoando aí!{/color}"
    hide kaito_box

    show player_box at left
    "{color=#0a0000}Oxi amigo, não tenho nada haver com o assunto.{/color}"
    hide player_box
    
    show padrao_box at left
    "{color=#0a0000}Kaito parecia um pouco frustrado e chateado e decidiu falar em um tom mais calmo.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Tudo bem então. Entendo o seu lado e sei que não gosta de perder tempo...{/color}"
    hide kaito_box

    show padrao_box at left
    hide kaito
    "{color=#0a0000}Ele saiu triste pela porta a procura da mochila.{/color}"
    hide padrao_box
    jump continuar3

label ajudar:
    show padrao_box at left
    play music "Missao Kaito.mp3"
    "{color=#0a0000}Falei entre risos e vejo Kaito ficando mais ansioso.{/color}"
    hide padrao_box
    
    show kaito_box at left
    "{color=#0a0000}Aaai [Nome]! Pelo amor de Deus!!! Me ajuda aí, para de rir! Mas agradeço pela ajuda de qualquer forma. Camila maldita!{/color}"
    hide kaito_box

    show padrao_box at left
    "{color=#0a0000}Eu me levantei rindo e fui com ele para o corredor procurar a mochila.{/color}"
    hide padrao_box
    scene corredor1
    show kaito at center
    show padrao_box at left
    "{color=#0a0000}A mochila não parecia estar lá.{/color}"
    hide padrao_box

    show kaito_box at left
    "{color=#0a0000}Ah mas que droga, espero que eu ache...{/color}"
    hide kaito_box
    hide kaito
    jump escolhas
label escolhas:
    scene corredor1
    show kaito
    show kaito_box at left
    menu:
        "{color=#0a0000}Certo, para onde vamos então?{/color}"

        "Cantina":
            jump ircantina
        "biblioteca":
            jump irbiblioteca
        "banheiro feminino":
            jump irbanheiro

label ircantina:
    hide kaito
    hide kaito_box
    scene cantina
    show kaito
    show player_box at left
    "{color=#0a0000}Parece que a mochila não está aqui.{/color}"
    hide player_box

    show kaito_box at left
    "{color=#0a0000}Mas que menina maldita! AAH falta 3 minutos pra professora chegar!{/color}"
    hide kaito_box

    show player_box at left
    "{color=#0a0000}Calma, vai dar tudo certo!{/color}"
    hide player_box

    show kaito_box at left
    "{color=#0a0000}Assim espero...{/color}"
    hide kaito_box
    hide kaito
    jump escolhas

label irbiblioteca:
    hide kaito
    hide kaito_box
    scene biblioteca
    show kaito
    show kaito_box at left
    "{color=#0a0000}Mas que ódio dessa babaca! Ah que ódio, a mochila não está aqui! {/color}"
    hide kaito_box
    jump escolhas

label irbanheiro:
    hide kaito
    hide kaito_box
    scene corredor1
    show kaito
    show kaito_box at left    
    "{color=#0a0000}Que droga!!!! Onde a mochila está?? Não me diga que....{/color}"
    hide kaito_box

    show player_box at left
    "{color=#0a0000}Acho que a Camila colocou...{/color}"
    hide player_box

    show padrao_box at left
    "{color=#0a0000}Então caminho até ao banheiro feminino.{/color}"
    hide padrao_box
    hide kaito

    scene banheiro
    show padrao_box at left
    show mochila
    "{color=#0a0000}Quando entrei lá eu vi uma mochila laranja.{/color}"
    "{color=#0a0000}entreguei para o Kaito{/color}"
    hide mochila
    hide padrao_box

    show kaito
    show kaito_box at left
    "{color=#0a0000}u não acredito, EU NÃO ACREDITO QUE ESSA GAROTA IMBECIL COLOCOU A MINHA MOCHILA NO BANHEIRO FEMININO, QUE ÓDIO DESSA GAROTA!{/color}"
    "{color=#0a0000}Olha, [Nome], muito obrigado de qualquer maneira! Agh até depois!{/color}"
    hide kaito_box
    hide kaito
    jump continuar3

label continuar3:
    scene salavazia
    play music "Sala de Aula ambientação.mp3"
    with fade
    show kaito at left
    show camilas at right
    show padrao_box at left
    "{color=#0a0000}Quando eu entrei na sala vi Kaito tirando satisfação com a Camila e reclamando.{/color}"
    hide padrao_box
    
    show kaito_box at left
    "{color=#0a0000}Eu sabia que foi você! Sua idiota!{/color}"
    hide kaito_box

    show padrao_box at left
    "{color=#0a0000}Ele falou quase chorando de raiva{/color}"
    hide padrao_box
    hide kaito
    show kaitos at left
    hide camilas 
    show camila at right
    show padrao_box at left
    "{color=#0a0000}Camila ficou rindo muito e depois começou a ficar preocupada.{/color}"
    hide padrao_box

    show camila_box at left
    "{color=#0a0000}F-Foi mal aí Kaito, eu não pensei que você ia...{/color}"
    hide camila_box
    hide camila
    show camilas at right
    hide kaitos
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}Agh, não importa! Tá perdoada. Ah mas que saco Camila! Que saco!!!{/color}"
    hide kaito_box
    hide kaito
    show kaitos at left
    hide camilas
    show camila at right
    show padrao_box at left
    "{color=#0a0000}Camila deu uma risada e depois pediu desculpas.{/color}"
    hide kaitos
    hide camila
    "{color=#0a0000}Depois disso, vi Jonathan tirando satisfação com a diretora e ele decidiu recorrer a quem??? A mim, a pessoa que não tem nada haver com o assunto (supostamente) mas tudo bem, né? As vezes parece que esse rapaz sabia que eu era detetive.{/color}"
    hide padrao_box
    show jonathan
    show jonathan_box at left
    "{color=#0a0000}Ei, garot[genero]!{/color}"
    hide jonathan_box
    show padrao_box at left
    "{color=#0a0000}Ele falou de uma forma mais rude para mim. Na hora comecei a sentir um frio na espinha, dizem que esse cara com homem ele briga fisicamente. Já com mulher dizem que ele faz de tudo para acabar com a reputação dela.{/color}"
    "{color=#0a0000}Ele não tinha muitos amigos na sala mas em outras ele tinha uma certa influência.{/color}"
    hide padrao_box

    show jonathan_box at left
    "{color=#0a0000}Seguinte, quer sair pra comer um lanche comigo?{/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Ufa... Não tinha sido nada de mais. Senti um alívio na alma.{/color}"
    hide padrao_box
    
    show player_box at left
    "{color=#0a0000}Talvez mais tarde.{/color}"
    hide player_box

    show padrao_box at left
    "{color=#0a0000}Jonathan sorriu pra mim.{/color}"
    hide padrao_box

    show jonathan_box at left
    "{color=#0a0000}Valeu aí! Cê é [um] [homem] que presta pelo menos. Diferente d[genero]s outr[genero]s imbecis. Você é foda!{/color}"
    hide jonathan_box
    show padrao_box at left
    "{color=#0a0000}Ele saiu de lá.{/color}"
    hide padrao_box
    hide jonathan

    scene biblioteca
    play music "Biblioteca ambientação.mp3"
    show padrao_box at left
    "{color=#0a0000}Decidi ir para a biblioteca para relaxar um pouco, quando vejo Marco e Jacob vindo em minha direção.{/color}"
    hide padrao_box
    show marco at left
    show jacobs at right
    show marco_box at left
    "{color=#0a0000}[Nome] você pode conversar com a gente?{/color}"
    hide marco_box
    hide marco
    show marcos at left
    hide jacobs
    show jacob at right
    show padrao_box at left
    "{color=#0a0000}Jacob parecia estar olhando pra mim com desdém.{/color}"
    hide padrao_box

    show jacob_box at left
    "{color=#0a0000}Não lembro de você...{/color}"
    hide jacob_box

    show player_box at left
    "{color=#0a0000}Como assim?{/color}"
    hide player_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Deixa, deixa pra lá, ele dormiu de bunda virada pra lua hoje eu acho.{/color}"
    hide marco_box
    hide marco
    show marcos at left
    hide jacobs
    show jacob at right
    show padrao_box at left
    "{color=#0a0000}Jacob olhou pra ele extremamente irritado.{/color}"
    hide padrao_box
    
    show jacob_box at left
    "{color=#0a0000}Cala a boca!!!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Ah, relaxa aí Jacob, você tá muito irritado. Seguinte, [Nome]! O Jacob tá passando mal, você poderia nos acompanhar até à enfermaria?{/color}"
    hide marco_box

    show player_box at left
    "{color=#0a0000}Claro!{/color}"
    hide player_box
    hide marco
    show marcos at left
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Tsk... Não quero ter aula com aquela baranga véia...{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Que...Ah Jacob tu não é assim não rapaz. Para de frescura, vai! {/color}"
    hide marco_box
    hide marco
    show marcos at left
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Ah mas que saco...{/color}"
    hide jacob_box

    show padrao_box at left
    "{color=#0a0000}Achei o comportamento do Jacob esquisito.{/color}"
    hide padrao_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show padrao_box at left
    "{color=#0a0000}Marco sorriu pra mim e falou baixo.{/color}"
    hide padrao_box
    
    show marco_box at left
    "{color=#0a0000}Relaxa, ele às vezes dá uns pitaco mesmo...{/color}"
    hide marco_box

    show player_box at left
    "{color=#0a0000}Então tudo bem né?{/color}"
    hide marco
    hide jacobs
    scene corredor3
    play music "Corredor-vazio ambientação.mp3"

    show marco at left
    show jacobs at right

    show padrao_box at left
    "{color=#0a0000}Marco sorriu para Jacob.{/color}"
    hide padrao_box

    show marco_box at left
    "{color=#0a0000}Você não é o rapaz que está passando mal? Vai lá pra enfermaria então cara.{/color}"
    hide marco_box
    hide marco
    show marcos at left
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Ah vai se ferrar Marco! Eu não vou pra lá não!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Você vai sim! Como você vai conseguir a licença pra poder não precisar ir pra aula?{/color}"
    hide marco_box
    hide marco
    show marco at left
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}De algum jeito eu arrumo mas não vai ser com essa porcaria de enfermaria!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show padrao_box at left
    "{color=#0a0000}Marco deu um sorriso de canto e deu uma cotoveladinha no Jacob.{/color}"
    hide padrao_box

    show marco_box at left
    "{color=#0a0000}Dizem que a enfermeira é uma tetéia, um pitelzinho.{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show padrao_box at left
    "{color=#0a0000}Os olhos de Jacob brilharam na hora mas ainda assim falou em um tom mal humorado.{/color}"
    hide padrao_box

    show jacob_box at left    
    "{color=#0a0000}Tá bom! Vou lá então!{/color}"
    hide marcos
    hide jacob

    scene enfermaria

    play music "Enfermaria ambientação.mp3"
    show marcos at left
    show jacob  at right
    show padrao_box at left 
    "{color=#0a0000}Entramos na enfermaria quando vimos uma velha caquética bem mal encarada.{/color}"
    hide padrao_box
    show reginas at center
    show padrao_box at left
    "{color=#0a0000}Jacob olhou para Marco horrorizado e com ódio.{/color}"
    hide padrao_box

    show jacob_box at left
    "{color=#0a0000} MARCO SEU FILHO DA PUTA!!! VOCÊ NÃO ME AVISOU QUE ERA UMA VÉIA CARCOMIDA!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    show padrao_box at left
    "{color=#0a0000}Marco deu uma risada alta e a enfermeira mal encarada olhou pro Jacob com ódio.{/color}"
    hide padrao_box
    hide reginas
    show regina at center
    show regina_box at left
    "{color=#0a0000}Vem logo, caralho, porra! Vem que vou te examinar! Anda logo, senta aqui!{/color}"
    hide regina_box
    hide regina
    show reginas at center
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Me trata com respeito, ameixa seca!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide reginas
    show regina at center
    show regina_box at left
    "{color=#0a0000}Olha só, você sabe que eu sou mais velha que você então me respeita porra! Seu vagabundo de merda! Você quer é matar aula né?{/color}"
    hide regina_box

    show padrao_box at left
    "{color=#0a0000}Enquanto estava acontecendo a confusão, eu vi um cinzeiro na mesa dela e olhei para os diplomas daquela enfermeira que parecia ser bem mal encarada.{/color}"
    '{color=#0a0000}Lá estava "Medicina veterinária" e "ciências contábeis", fiquei um tanto espantada, mas o que??{/color}'
    hide padrao_box
    hide regina
    show reginas at center
    hide marcos
    show marco at left
    show padrao_box at left
    "{color=#0a0000}Falei no ouvido do Marco.{/color}"
    hide padrao_box

    show player_box at left
    "{color=#0a0000}Eu olhei para o diploma e... ela é formada pra ser veterinária.{/color}"
    hide player_box

    show marco_box at left
    "{color=#0a0000}Escolheram ela só pra preencher o buraco que tinha, porque muito aluno tava querendo matar aula aí mentia na secretaria falando que estava passando mal. Essa véia aí não sabe de nada.{/color}"
    hide marco_box

    show player_box at left
    "{color=#0a0000}Vish... então...{/color}"
    hide player_box

    show padrao_box at left
    "{color=#0a0000}Olhei pra enfermeira meio desconfiada, o Jacob ficou revoltadíssimo e ficou se debatendo.{/color}"
    hide padrao_box
    hide marco
    show marcos at left
    hide reginas
    show regina at center
    show regina_box at left
    "{color=#0a0000}Cala a boca que eu vou escutar a tua pressão seu vagabundo! Senta aí!{/color}"
    hide regina_box
    hide regina
    show reginas at center
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Escutar a minha pressão? Onde??? Que?!?!?{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    show padrao_box at left
    "{color=#0a0000}Ela pegou um telefone e colocou a parte maior onde ficavam os números da no peito dele e a parte que escuta no ouvido dela.{/color}"
    hide padrao_box
    hide reginas
    show regina at center
    show regina_box at left    
    "{color=#0a0000}Agora respira! {/color}"
    hide regina_box
    hide regina
    show reginas at center
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Aah não sei se tu é capacitada mesmo não, mulher!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide reginas
    show regina at center
    show regina_box at left
    "{color=#0a0000}Eu me formei em duas faculdades, então cala a sua boca, seu vagabundo!{/color}"
    hide regina_box
    hide regina
    show reginas at center
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Mas que cheiro de cigarro...{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide reginas
    show regina at center
    show regina_box at left
    "{color=#0a0000}CALA A BOCA!{/color}"
    hide regina_box
    hide regina
    show reginas at center
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Mas que saco! Velha vagabunda!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide reginas
    show regina at center
    show regina_box at left
    "{color=#0a0000}Seguinte, se você tem força pra reclamar, tem força pra continuar na aula também, sai daqui ou vai tomar advertência!{/color}"
    hide regina_box
    hide regina
    show reginas at center
    hide jacobs
    show jacob at right
    show jacob_box at left    
    "{color=#0a0000}E tu vai tomar demissão, véia rabugenta!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right

    show padrao_box at left
    "{color=#0a0000}A enfermeira olhou pra ele com um olhar de morte e gritou.{/color}"
    hide padrao_box
    hide reginas
    show regina at center
    show regina_box at left
    "{color=#0a0000}SAI DAQUI! VOCÊS TRÊS!{/color}"
    hide regina_box
    hide jacobs
    hide marcos
    hide regina
    scene cantina
    play music "Cantina ambientação.mp3"

    show marco at left
    show jacobs at right
    show padrao_box at left
    "{color=#0a0000}Após isso a gente decidiu ir pra cantina e decidimos conversar.{/color}"
    "{color=#0a0000}Marco estava rindo e Jacob estava irritado.{/color}"
    hide padrao_box

    show marco_box at left    
    "{color=#0a0000}O que acha da tetéia?{/color}"
    hide marco_box
    hide marco
    show marcos at left
    hide jacobs
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Igual sua mãe, só se for né? Seu arrombado!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    show padrao_box at left    
    "{color=#0a0000}Marco olhou espantado e riu um pouco.{/color}"
    hide padrao_box
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Calma, calma... Ninguém precisa ofender a mãe de ninguém não, tá?{/color}"
    hide marco_box
    hide marco
    show marcos at left
    show padrao_box at left    
    "{color=#0a0000}Após isso, vi Jonathan e Astrid fazendo um sinal pra vir até eles.{/color}"
    hide padrao_box

    show player_box at left
    "{color=#0a0000}Gente, acho que eles estão me chamando para alguma coisa, jajá falo com vocês.{/color}"
    hide player_box
    hide marcos
    hide jacobs

    scene escolafeio
    play music "Escola-canto-feio ambientação.mp3"
    show astrid at left
    show jonathans at right
    show astrid_box at left
    "{color=#0a0000}Então, [Nome]. Nós temos um assunto importante pra falar com você.{/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}Eu mando o papo ou você manda?{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide astrids
    show astrid at left
    show astrid_box at left
    "{color=#0a0000}O que você achar melhor.{/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    hide jonathans
    show jonathan at right
    show jonathan_box at left    
    "{color=#0a0000}Ok, então eu falo pra ser melhor.{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide astrids
    show astrid at left
    show astrid_box at left
    "{color=#0a0000}Agh como eu detesto essa sua atitude pretenciosa.{/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}Pretencioso?? Nem sei o que significa e tô pouco me fodendo também. Ah, mas que saco! {/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Jonathan olhou para mim sério e Astrid também.{/color}"
    hide padrao_box

    show jonathan_box at left
    "{color=#0a0000}Seguinte,[Nome]. Nós descobrimos coisinhas sobre você enquanto eu e a Astrid decidimos ver suas coisas.{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    show player_box at left    
    "{color=#0a0000}Espera... Vocês fuçaram minhas coisas???{/color}"
    hide player_box
    hide astrids
    show astrid at left
    show astrid_box at left
    "{color=#0a0000}Seja mais educad[genero]! Sim, mexemos nas suas coisas pra descobrir sobre você. {/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}É! E digamos que... Quando te chamei para o lanche, se lembra? Então... Era pra botar uns assuntos em dia, e você é um idiota mesmo hein? Descobrimos algumas coisinhas...{/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Fiquei tremendo um tanto. Um medo começou a correr por mim, fiquei tens[genero] de certa forma.{/color}"
    hide padrao_box
    hide jonathan
    show jonathans at right
    hide astrids
    show astrid at left
    show astrid_box at left
    "{color=#0a0000}Não adianta esconder de nós! Você então é [um] detetive huh? {/color}"
    hide astrid_box

    show padrao_box at left
    "{color=#0a0000}Ela falou em um tom sarcástico.{/color}"
    hide padrao_box

    show astrid_box at left
    "{color=#0a0000}Descobrimos isso lendo fichas e... Você suspeita da gente? Ah que pena...{/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    hide jonathans
    show jonathan at right
    show padrao_box at left
    "{color=#0a0000}Jonathan falou em um tom de ameaça {/color}"
    hide padrao_box

    show jonathan_box at left
    "{color=#0a0000}Você sabe da minha reputação então??? Se tu tentar me botar em cana tu tá fodid[genero] na minha mão.{/color}"
    
    if genero=="o":
        "{color=#0a0000}Farei questão de te deitar na porrada e te mandar pro hospital.{/color}"
    if genero=="a":
        "{color=#0a0000}Não costumo bater em mulheres, mas para você eu abriria uma exceção.{/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Eu fiquei com tanto medo...{/color}"
    hide padrao_box
    hide jonathan
    show jonathans at right
    hide astrids
    show astrid at left
    show astrid_box at left
    "{color=#0a0000}E eu mesmo sendo mais da lei, apoio essa ideia. Enquanto Jonathan te bate, posso acabar com sua reputação de alguma forma, então é melhor não tentar nos colocar na cadeia.{/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}Não estraga as coisas, Astrid. Isso só vai piorar, deixa de ser imbecil!{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide astrids
    show astrid at left
    show astrid_box at left    
    "{color=#0a0000}Então vai procurar o que fazer! Você não tem o mínimo de moral, viu?{/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}E eu ligo pra isso?  {/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Jonathan olhou para mim sério.{/color}"
    hide padrao_box

    show jonathan_box at left
    "{color=#0a0000}Sobre a Olívia, ela era uma inútil mesmo, eu era o cara que ela achava que valorizava ela. Ela pra mim era apenas mais uma putinha inútil pra passar o tempo.{/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Eu olhei com um ódio imenso pra ele e respirei pesado.{/color}"
    hide padrao_box

menu:
    "Você não passa de um ser desprezível, Jonathan! Um ser tão nojento com uma moral tão destorcida, você só pensa em si mesmo! Eu quero muito que você queime no inferno!":
        jump xingou

    "Eu optei por manter a calma.":
        jump calma

label xingou:
    show padrao_box at left
    "{color=#0a0000}Jonathan não pensou duas vezes e tentou ir pra cima de mim. Admito que senti vontade de socar ele também, mas Astrid interveio e segurou Jonathan.{/color}"
    hide padrao_box
    hide jonathan
    show jonathans at right
    hide astrids
    show astrid at left
    show astrid_box at left
    "{color=#0a0000}Jonathan, [genero] [Nome] infelizmente está certo sobre isso, você precisa ser mais controlado, você trata todo mundo feito um lixo e acha que a vida é em função de você!{/color}"
    "{color=#0a0000}Se for partir pra violência, isso não vai te levar a nada, só vai piorar sua situação e aí sim você vai pra cadeia.{/color}"
    hide astrid_box
    hide astrid
    show astrids at left
    show padrao_box at left
    "{color=#0a0000}Jonathan fecha os punhos e treme de raiva, depois suspira e apenas fala com um pouco mais de calma.{/color}"
    hide padrao_box
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}Tudo bem! Mas para de falar bosta sobre mim, tá? Você não me conhece, não sabe o que passei, então cala a porra dessa sua boca!{/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Ele se virou de costas e saiu junto com Astrid{/color}"
    hide jonathan
    hide astrids
    hide padrao_box
    jump continuar4

label calma:
    show padrao_box at left
    "{color=#0a0000}Astrid parecia estar um pouco tensa e Jonathan olhou para mim irritado mas sorriu.{/color}"
    hide padrao_box
    
    show jonathan_box at left   
    "{color=#0a0000}Ah que bom, ficou quietinh[genero] né? Fica assim mesmo, conselho de amiguinho. Melhor abaixar suas orelhas mesmo e sair com o rabo entre as pernas, pra não ir embora com sua costela quebrada.{/color}"
    hide jonathan_box

    show padrao_box at left
    "{color=#0a0000}Eu virei de costas furios[genero] e caminhei em direção à saída{/color}"
    hide padrao_box
    hide jonathan
    hide astrids
    scene ato3
    " "
    jump continuar4
#------------------------------------------------------ato3---------------------------------------------------------------------------------
label continuar4:
    scene salavazia
    play music "Sala de Aula ambientação.mp3"
    show padrao_box at left
    "{color=#0a0000}Haviam se passado 5 meses, deu tempo o suficiente de eu ter me aproximado da Camila, e sobre aquilo que o Jonathan disse, tenho que admitir que havia me perturbado. Aquele cara realmente era muito podre. {/color}"
    "{color=#0a0000}Me senti intimidad[genero] de fato e ele estava sendo um dos principais suspeitos, mesmo se ele não for o assassino, ele com certeza vai pra cadeia, nem que seja por meses. Ele está por um fio na justiça. Além da ansiedade aumentando porque eu ainda não consegui resolver o caso.{/color}"
    hide padrao_box
    show camila at center
    show padrao_box at left
    "{color=#0a0000}Meus pensamentos de repente foram interrompidos por Camila querendo conversar comigo.{/color}"
    hide padrao_box
    show camila_box at left    
    "{color=#0a0000}[Nome], eu preciso falar um negócio.{/color}"
    hide camila_box
    show player_box at left
    "{color=#0a0000}Sim? Pode falar.{/color}"
    hide player_box
    show camila_box at left
    "{color=#0a0000}Bem... Agh que imbecil o que vou dizer, mas ok, lá vai: Eu não sou uma pessoa sentimental, você sabe disso, mas...{/color}"
    hide camila_box
menu:
    "Ai! Para de enrolar e fala logo!":
        jump fala
    "Tenha seu tempo, espero que esteja bem.":
        jump enrola
label fala:
    show padrao_box at left
    "{color=#0a0000}Camila me olhou com raiva.{/color}"
    hide padrao_box
    show camila_box at left
    "{color=#0a0000}Impaciente hein? Calma, amor!{/color}"
    hide camila_box
    jump continuar5
label enrola:
    show padrao_box at left
    "{color=#0a0000}Camila sorriu para mim{/color}"
    hide padrao_box
    show camila_box at left
    "{color=#0a0000}Obrigada por me entender, bem, então eu vou dizer....{/color}"
    hide camila_box
    jump continuar5
label continuar5:
    show camila_box at left
    "{color=#0a0000}Acho que estou apaixonada pelo kaito, acredito que minhas brincadeiras com ele foram uma tentativa fracassada de tentar conquistar ele.{/color}"
    hide camila_box
    hide camila
    show camilas at left
    show padrao_box at left
    "{color=#0a0000}Após isso eu ouvi uma risada e vi que Astrid chegou se intrometendo.{/color}"
    hide padrao_box
    show astrid at right
    show padrao_box at left
    "{color=#0a0000}Ela disse com um sorriso malicioso.{/color}"
    hide padrao_box
    show astrid_box at left
    "{color=#0a0000}Ah, então está apaixonadinha pelo Kaito, Camila?{/color}"
    hide astrid
    hide astrid_box
    show astrids at right
    hide camilas
    show camila at left
    show camila_box at left
    "{color=#0a0000}Se manca, sua puta, você tem namorado porra!{/color}"
    hide camila_box
    hide astrids
    show astrid at right
    hide camila
    show camilas at left
    show astrid_box at left
    "{color=#0a0000}Pelo seu linguajar, acho que vou... Tentar algo. Estou insatisfeita com o Jonathan.{/color}"
    hide astrid_box
    show padrao_box at left
    "{color=#0a0000}Jonathan tinha olhado para Astrid com um ódio mortal enquanto Astrid estava sorrindo.{/color}"
    "{color=#0a0000}Astrid virou para trás e olhou para Kaito que estava sentado na frente e sorriu.{/color}"
    hide padrao_box
    show kaitos at center
    show astrid_box at left
    "{color=#0a0000}Kaito!!! Você quer sair comigo hoje?{/color}"
    hide astrid
    show astrids at right
    hide kaitos
    show kaito at center
    hide astrid_box
    show padrao_box at left
    "{color=#0a0000}Kaito rapidamente se levantou e sorriu para ela.{/color}"
    hide padrao_box
    show kaito_box at left
    "{color=#0a0000}C-claro!!! Aceito sim!{/color}"
    hide kaito_box
    hide kaito
    hide astrids
    show astrid at right
    show astrid_box at left
    "{color=#0a0000}Então combinado!{/color}"
    hide astrid_box
    show padrao_box at left
    "{color=#0a0000}Camila depois olhou para Astrid com um ódio e Astrid ficou rindo e saiu de lá.{/color}"
    hide padrao_box
    hide kaitos
    hide astrid
    hide camilas
    show camila
    show camila_box at left
    "{color=#0a0000}Ela vai pagar por isso.{/color}"
    hide camila_box
    hide camila
    show player_box at left
    "{color=#0a0000}Espera, Camila! Não faça nada precipitado!{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Quando falei isso, me dei conta que ela já havia saído.{/color}"
    "{color=#0a0000}Após isso, Marco chegou perto de mim  e se sentou ao meu lado.{/color}"
    hide padrao_box
    show marco at right
    show marco_box at left
    '{color=#0a0000}Vai dar tudo certo, ah! Se precisar de alguma coisa sobre as pessoas, só me chamar. Sou "amigo" praticamente de todo mundo aqui, então se precisar de alguma informação é só me chamar.{/color}'
    hide marco_box
    show player_box at left
    "{color=#0a0000}Muito obrigado!{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Marco sorriu gentilmente.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}De nada!{/color}"
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Marco saiu de lá.{/color}"
    hide marco
    "{color=#0a0000}A minha atenção então foi desviada por uma cena um tanto inusitada.{/color}"
    hide padrao_box
    show kaito at left
    show kaito_box at left
    "{color=#0a0000}Vocês querem saber de algo sombrio? Eu aconselho não mexer comigo, principalmente em lua cheia!!! Ontem à noite eu virei um lobisomem! Vocês deveriam me temer de verdade!{/color}"
    hide kaito_box
    hide kaito
    show kaitos at left
    show jonathan at right
    show padrao_box at left
    "{color=#0a0000}Jonathan ficou rindo de canto.{/color}"
    hide padrao_box
    show jonathan_box at left
    "{color=#0a0000}Lobisomem é? Você agora vai contar amanhã o que? Que vai virar o cabeça de cuia ???{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide kaitos
    show kaito at left
    show padrao_box at left
    "{color=#0a0000}Kaito se enfureceu. Ele falou para Jonathan em um tom ameaçador.{/color}"
    hide padrao_box
    show kaito_box at left
    "{color=#0a0000}Irei fazer seu sangue espirrar pelo seu pescoço e...{/color}"
    hide kaito
    hide kaito_box
    show kaitos at left
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}E eu quebro o seu antes que você possa relar um dedo em mim!{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide kaitos
    show kaito at left
    show padrao_box at left
    "{color=#0a0000}Kaito demonstrou um medo mas tentou esconder isso.{/color}"
    hide padrao_box
    show kaito_box at left
    "{color=#0a0000}Você vai ver só! Pode vir pra...{/color}"
    hide kaito_box
    hide kaito
    show kaitos at left
    show padrao_box at left
    "{color=#0a0000}Marco interveio segurando Kaito.{/color}"
    hide padrao_box
    show marco at center
    show marco_box at left
    "{color=#0a0000}Opa opa opa... Calma lá Kaito! Vamos pensar nisso depois? Desculpa, Jonathan, o Kaito as vezes quer dar uma de valente mas ele não te odeia.{/color}"
    hide marco_box
    hide marco
    show marcos at center
    hide jonathans
    show jonathan at right
    show jonathan_box at left
    "{color=#0a0000}Não me odeia é? Tá bom, que se foda, eu não ligo pra esse merda de qualquer maneira.{/color}"
    hide jonathan_box
    show padrao_box at left
    "{color=#0a0000}Jonathan falou dando as costas.{/color}"
    hide padrao_box
    hide jonathan
    hide marcos
    hide kaitos
    scene corredor1
    play music "Corredor ambientação.mp3"
    show padrao_box at left
    "{color=#0a0000}Depois disso teve mais aulas e mais aulas até que deu o horário do fim das aulas. Decidi ir para o corredor e vi Jacob e Marco.{/color}"
    hide padrao_box
    show marcos at right
    show jacobs at left
    show padrao_box at left
    "{color=#0a0000}Jacob parecia ter novamente estar irritado.{/color}"
    hide marcos
    hide padrao_box
    show marco at right
    show marco_box at left
    "{color=#0a0000}Ah Jacob, por que você tá assim? Você não quer nem conversar tanto, tá chateado?{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Não foi nada. Deixa pra lá.{/color}"
    hide jacob
    show jacobs at left
    hide jacob_box
    show padrao_box at left
    "{color=#0a0000}Ele falou em um tom seco, mas tentando esconder o que ele estava sentindo.{/color}"
    hide padrao_box
    hide marcos
    show marco at right
    show marco_box at left
    "{color=#0a0000}Tem certeza?{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Eu disse que não foi nada, pode ficar tranquilo, de verdade!{/color}"
    hide jacob_box
    show player_box at left
    "{color=#0a0000}Tudo bem com você?{/color}"
    hide player_box
    show jacob_box at left
    "{color=#0a0000}Não, nada! Sério mesmo.{/color}"
    hide jacob_box
    show padrao_box at left
    "{color=#0a0000}Jacob parecia ainda assim falar em um tom seco.{/color}"
    hide padrao_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show marco_box at left
    "{color=#0a0000}PUTZ, VERDADE! AH RAPAZ, SEU ANIVERSÁRIO FOI ONTEM NÉ???{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Aaah agora você adivinhou??? E quer saber de algo? Ninguém lembrou do meu aniversário!{/color}"
    hide jacob_box
    hide jacob
    show jacobs at left
    hide marcos
    show marco at right
    show marco_box at left
    "{color=#0a0000}Me desculpa de verdade!{/color}"
    hide marco_box
    hide marco
    show marcos at right
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Não, tá tudo bem. O triste é que ninguém me deu parabéns ontem. Isso me deixou realmente mal, eu lembro do aniversário de todo mundo!{/color}"
    hide jacob
    hide jacob_box
    show jacobs at left
    hide marcos
    show marco at right
    show marco_box at left
    "{color=#0a0000}Me desculpa mesmo, de verdade.{/color}"
    hide marco
    show marcos at right
    hide marco_box
    hide jacobs
    show jacob at left
    show jacob_box at left
    "{color=#0a0000}Já foi!!! Agora que se dane! Ninguém nunca vai se importar comigo mesmo!{/color}"
    hide jacob_box
    show padrao_box at left
    "{color=#0a0000}Ele falou dando as costas e correndo.{/color}"
    hide padrao_box
    hide jacob
    hide marcos
    show marco at center
    show marco_box at left
    "{color=#0a0000}Agh... Jacob pera aí...{/color}"
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Jacob já havia saído e Marco virou para mim e falou.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}Me desculpa pelo jeito do Jacob. Ele as vezes dá os pitacos dele.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Eu percebi isso muito bem hein?{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Eu ri um pouco e ele também.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}Mas ele não é toda hora assim não. Só 80%% do tempo. {/color}"
    hide marco_box
    show padrao_box at left    
    "{color=#0a0000}Ele falou entre risos.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}Ele uma vez ficou sem falar comigo porque eu tinha rido que ele tinha matado um gafanhoto bebezinho achando que era um mosquito.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Eu não consigo me esquecer do evento da enfermeira.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Acredita que ele esqueceu? Sabe, mas naquele momento, ele deu uma sorte lascada. Já vi relatos que aquela véia já tentou colocar termômetro retal em algumas pessoas.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Misericórdia!{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Nós rimos um pouco mas senti que eu precisava falar algo importante para o Marco.{/color}"
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Marco, preciso colocar algumas coisas sobre a mesa que guardei por muito tempo.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Hum?{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Embora eu seja [um] profissional, não significa que eu não me importe com vocês, muito pelo contrário, acho que desenvolvi uma certa amizade por vocês.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Que bom! Fico feliz de verdade!!! Também te considero bastante.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Agradeço... Mas enfim. Você sabe o Jonathan, certo? Tenho que admitir que deixei minhas emoções tomarem conta de mim no momento, mas enfim. Ele acabou me intimidando.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Ah sim, novidade? Nenhuma. Típco, mas não é tão à tôa, tá, não é necessário o que ele faz. A família dele é toda quebrada.{/color}"
    "{color=#0a0000}A mãe dele largou ele com o pai quando criança como se o Jonathan não tivesse importância por causa que ela estava com outro homem e o pai era um alcoólatra.{/color}"
    "{color=#0a0000}Além de depois o pai dele ter achado uma mulher lá que vivia brigando e esnobando o Jonathan perante os meio irmãos dele.{/color}"
    "{color=#0a0000}Mas enfim, ele trata a gente como se tivéssemos culpa da vida desestruturada dele e isso que eu não acho legal.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Sinto muito pelo Jonathan, mas mesmo assim, creio que ele precisa se portar melhor.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}De fato. Mas creio que Jonathan é um forte suspeito sim. Porque ele já namorou Olivia e ela tinha uma consideração muito grande por ele, porém, para Jonathan, ela não passava de mais um passa-tempo para ele.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Sim, eu sei, ele teve a coragem de dizer isso para mim.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Ele foi babaca, de qualquer maneira.{/color}"
    hide marco_box
    hide marco

    scene salavazia
    play music "Sala de Aula ambientação.mp3"

    show padrao_box at left
    "{color=#0a0000}Assim que voltei para a sala, vi Camila extremamente assustada e com as mãos ensanguentadas. Eu fiquei um tanto perplexo também.{/color}"
    hide padrao_box
    show camila
    show player_box at left
    "{color=#0a0000}O que foi Camila?? O que aconteceu???{/color}"
    hide player_box
    show camila_box at left
    "{color=#0a0000}A Astrid... Ela... ela morreu! O pescoço dela tá todo cortado! Eu tentei socorrer ela mas era tarde de mais.{/color}"
    hide camila_box
    show player_box at left
    "{color=#0a0000}Tá mas onde você viu ela morta???{/color}"
    hide player_box
    show camila_box at left
    "{color=#0a0000}No banheiro feminino.{/color}"
    hide camila_box
    show player_box at left
    "{color=#0a0000}Ok, liga pra polícia o mais rápido possível.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Camila não pensou duas vezes e correu para uma cabine telefônica. Um monte de alunos correram e perguntaram o porquê das mãos ensanguentadas e a expressão assustada.{/color}"
    "{color=#0a0000}Camila apenas disse que depois explicava, ela parecia tremer muito enquanto ligava. Após isso, corremos para o banheiro.{/color}"
    hide padrao_box
    hide camila

    scene banheiroastrid
    play music "Banheiro ambientação.mp3"

    show padrao_box at left
    "{color=#0a0000}Eu e Camila quando chegamos lá, vimos a mão de Astrid atrás da cabine e uma enorme mancha de sangue borrando o chão e a parede. Sons das sirenes da polícia dominaram o local e a escola virou uma verdadeira baderna.{/color}"
    hide padrao_box

    scene corredor3
    play music "Corredor-vazio ambientação.mp3"
    show padrao_box at left
    "{color=#0a0000}Vi Marco um tanto perplexo também.{/color}"
    show marco at left
    show camilas at right
    show marco_box at left
    "{color=#0a0000}Ei, tá tendo um monte de polícia aqui, o que aconteceu?{/color}"
    hide marco
    hide marco_box
    show marcos at left
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}Marco, a Astrid ela... Ela foi assassinada!!!!{/color}"
    hide camila_box
    hide camila
    show camilas at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}O que??? Gente, o buraco então era bem mais fundo do que eu pensava, acho que realmente tem um assassino a solta por aqui.{/color}"
    "{color=#0a0000}Admito que com a Olívia eu já estava proecupado até porque pelo estado dela eu suspeitava que era suicídio, mas agora com a Astrid morta... Pelo jeito temos um assassino a solta.{/color}"
    hide marco_box
    hide marco
    hide camilas
    scene ato4
    " "
#===================================================================================final ato 3--------------------------------------------------------------------------------------------------------
    scene cantina
    play music "Cantina ambientação.mp3"
    show marcos at left
    show camilas at right
    show player_box at left
    "{color=#0a0000}Marco, posso fazer algo?{/color}"
    hide player_box
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Sim? Mas me diga o que quer fazer.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Abrir o Jogo pra Camila.{/color}"
    hide player_box
    hide Marco
    show marcos at left
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}Do que vocês estão falando? Estão escondendo algo de mim?{/color}"
    hide camila_box
    show padrao_box at left
    "{color=#0a0000}Eu respirei fundo e falei.{/color}"
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Eu sou [um] detetive e tive que me infiltrar pra poder resolver o caso da morte da Olívia.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Camila parecia estar em choque e logo sua expressão começou a se tornar uma raiva eminente.{/color}"
    hide padrao_box
    show camila_box at left
    "{color=#0a0000}O QUE??? AH EU NÃO ACREDITO! Eu pensava que você era meu amigo de verdade, mas que ódio! Então quer dizer que você usou as emoções dos outros ao seu favor por causa de um trabalho?{/color}"
    "{color=#0a0000}Marco e sobre você? Tu sabia desde o começo provavelmente e mesmo assim tu aceitou de boa? {/color}"
    hide camila_box
    hide camila
    show camilas at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Calma Camila. el[e] não fez por mal.{/color}"
    hide marco
    show marcos at left
    hide camilas
    show camila at right
    hide marco_box
    show camila_box at left
    "{color=#0a0000}Oh! E como eu não desconfiei da informação del[e] ser [um] detetive??? Eu já entendi logo de primeira, como assim???{/color}"
    hide camila_box
    hide camila
    show camilas at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Porque somos a porcaria de personagens de um jogo! Agora segue o barco!{/color}"
    hide marco 
    show marcos at left
    hide camilas
    show camila at right
    hide marco_box
    show camila_box at left
    "{color=#0a0000}Ah tá. Mas que saco!{/color}"
    hide camila_box
    hide camila
    show camilas at right
    show player_box at left
    "{color=#0a0000}Mas Camila, não me leve a mal. Eu te considero bastante, de verdade e estamos na mesma, eu preciso desvendar quem é o assassino pra proteger vocês, além disso, acabei sim de fato me apegando a vocês.{/color}"
    hide player_box
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Exatamente!{/color}"
    hide marco
    show marcos at left
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Camila me olhou meio apreensiva e deu um suspiro.{/color}"
    hide camilas
    show camila at right
    hide padrao_box
    show camila_box at left
    "{color=#0a0000}Ah que se dane! Tudo bem, tudo bem. Esse tá sendo literalmente o pior dia da minha vida, mas me faça as perguntas então logo! Anda!{/color}"
    hide camila_box
    show player_box at left
    "{color=#0a0000}Então tudo bem. Eu descobri que você tinha uma leve apatia pela Astrid, ainda mais por conta daquele evento que ela deu em cima do garoto que você gosta. Você sentiu alguma vontade de acabar com ela?{/color}"
    hide player_box
    show camila_box at left
    "{color=#0a0000}Eu tenho que admitir que eu odiava aquela baranga, mas em hipótese alguma eu faria isso com ela!{/color}"
    "{color=#0a0000}Eu embora tenha uma personalidade forte, eu raramente vou partir pro soco com alguém, na verdade nunca me ocorreu um troço desses.{/color}"
    hide camila_box
    hide camila
    show camilas at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Ela tem razão, estranhamente eu nunca vi a Camila brigar na escola.{/color}"
    hide marco
    show marcos at left
    hide marco_box
    show player_box at left
    "{color=#0a0000}Oh, isso é bom! Camila, sobre o momento que Astrid morreu. Me diz como foi, como você se deparou com o corpo dela.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Camila respirou fundo novamente, ela estava um pouco tensa e ainda parecia chocada.{/color}"
    hide padrao_box
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}Certo. Eu estava o tempo todo na cantina colando adesivos no meu caderno com algumas amigas e achei meio estranho que Astrid não tinha passado pra comprar lanche.{/color}"
    "{color=#0a0000}Até que eu fui no banheiro porque eu tava apertada e aí me deparei com a Astrid caída ensanguentada no chão. Ela estava morrendo. Ela disse que não esperava que ele iria tão longe.{/color}"
    hide camila
    show camilas at right
    hide marcos
    show marco at left
    hide camila_box
    show marco_box at left
    "{color=#0a0000}Ele quem???{/color}"
    hide camilas
    show camila at right
    hide marco
    show marcos at left
    hide marco_box
    show camila_box at left
    "{color=#0a0000}Ela não disse, antes dela exibir a primeira sílaba,ela se foi.{/color}"
    hide camila
    show camilas at right
    hide marcos
    show marco at left
    hide camila_box
    show marco_box at left
    '{color=#0a0000}Ela disse que não esperava que "Ele" iria tão longe.{/color}'
    hide marco
    show marcos at left
    hide marco_box
    show player_box at left
    "{color=#0a0000}Parece que tudo se encaixa agora! Obrigada Camila! Ah! Te tirei da lista de suspeitos.{/color}"
    hide player_box
    hide camilas
    show camila at right
    show camila_box at left
    "{color=#0a0000}Valeu...{/color}"
    hide camila
    hide camila_box
    show padrao_box at left
    "{color=#0a0000}Camila foi embora, só ficando eu e o Marco na escadaria.{/color}"
    hide padrao_box
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}[Nome], já foram 2 pessoas mortas nessa escola! Eu juro que não medirei esforços para te ajudar nesse caso e não vou descansar até encontrar o assassino! Esse filho da puta vai ter que pagar!{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Muito obrigada, de verdade.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}[Nome], vê se é uma boa ideia, você pode anunciar que é a detetive para a sala e aí você chama os suspeitos para interrogar.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Acho uma boa ideia.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Então fomos atrás dos suspeitos. O primeiro foi o Kaito.{/color}"
    hide padrao_box
    hide marco

    scene salavazia
    play music "Sala de Aula ambientação.mp3"
    show padrao_box at left
    "{color=#0a0000}Corremos até ele que estava bastante tenso e assustado.{/color}"
    hide padrao_box
    show marcos at left
    show kaito at right
    show kaito_box at left
    "{color=#0a0000}Eu vou achar quem matou a Astrid e vou acabar com ele!!!{/color}"
    hide kaito_box
    hide kaito
    show kaitos at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Kaito!{/color}"
    hide marco_box
    hide kaitos
    show kaito at right
    hide marco
    show marcos at left
    show kaito_box at left
    "{color=#0a0000}Isso não pode ser verdade, ela deve estar pregando uma peça na gente, se não for, vou fazer o assassino implorar pela vida e...{/color}"
    hide kaito_box
    hide kaito
    show kaitos at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}KAITO! Presta atenção!!!{/color}"
    hide marco_box
    hide kaitos
    show kaito at right
    hide marco
    show marcos at left
    show padrao_box at left
    "{color=#0a0000}Kaito finalmente se virou para nós.{/color}"
    hide padrao_box
    show kaito_box at left
    "{color=#0a0000}Hum?{/color}"
    hide kaito_box
    hide kaito
    show kaitos at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}O [Nome] tem algo pra falar pra ti.{/color}"
    hide marco_box
    hide kaitos
    show kaito at right
    hide marco
    show marcos at left
    show kaito_box at left
    "{color=#0a0000}Estou ocupado com meu plano de vingança.{/color}"
    hide kaito_box
    show player_box at left
    "{color=#0a0000}Kaito é uma coisa séria, eu peço que me ouça.{/color}"
    hide player_box
    show kaito_box at left
    "{color=#0a0000}Então me diz o que quer falar.{/color}"
    hide kaito_box
    show player_box at left
    "{color=#0a0000}Eu sou [um] detetive que está infiltrad[genero] na escola.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Eu falei mostrando meu documento comprovando que eu era um detetive.{/color}"
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Estou trabalhando no caso da morte de Olívia e agora também o da Astrid. Você está dentre os suspeitos.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Kaito olhou pra mim assustado e começou a entrar em desespero e chorar.{/color}"
    hide padrao_box
    show kaito_box at left
    "{color=#0a0000}PELO AMOR DE DEUS EU NÃO FIZ NADA, EU JURO PELA MINHA VIDA! EU NUNCA QUIS MATAR NINGUÉM, EU SOU UM PROTETOR, EU JURO POR DEUS QUE NÃO FIZ NADA!{/color}"
    hide kaito_box
    show player_box at left
    "{color=#0a0000}Ei Kaito, calma, respira.{/color}"
    hide player_box
    show kaito_box at left
    "{color=#0a0000}Essa situação toda me deixou ansioso, eu nunca quis ver a morte de ninguém aqui! Eu...eu...{/color}"
    hide kaito_box
    hide kaito
    show kaitos at right
    show padrao_box at left
    "{color=#0a0000}Marco colocou a mão nas costas de Kaito e olhou para ele, a expressão de Marco parecia reconfortante.{/color}"
    hide padrao_box
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Ei, tá tudo bem. Tenho que admitir que quando conheci [genero] [Nome] e descobri logo de cara que el[e] era [um] detetive, fiquei bem ansioso e agi mal também.{/color}"
    "{color=#0a0000}Mas [genero] [Nome] só porque suspeita de você, não significa que el[e] vai te prender injustamente.{/color}"
    "{color=#0a0000}[genero] [Nome] só suspeita de você porque era mais próximo da Olívia, assim como eu, Camila, Astrid... El[e] não vai te prender, pode ficar tranquilo, viu?{/color}"
    hide marco_box
    hide marco
    show marcos at left
    show padrao_box at left
    "{color=#0a0000}Kaito parecia ter se acalmado um pouco e respirou fundo.{/color}"
    hide padrao_box
    hide kaitos
    show kaito at right
    show kaito_box at left
    "{color=#0a0000}Pode me perguntar tudo que for possível. Vou responder com honra.{/color}"
    hide kaito_box
    show padrao_box at left
    "{color=#0a0000}Eu sorri para ele pra tranquilizar, então perguntei.{/color}"
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Kaito, onde você estava quando Astrid supostamente tinha sido assassinada?{/color}"
    hide player_box
    show kaito_box at left
    "{color=#0a0000}Eu estava na biblioteca como sempre, eu gosto de passar meu tempo lá lendo alguns livros, a Astrid durante o intervalo costumava ficar na biblioteca também, mas ela não estava, isso que achei esquisito.{/color}"
    "{color=#0a0000}Fiquei mais um tempo lendo até que ouvi as pessoas fazendo barulho do lado de fora, fiquei irritado porque estava atrapalhando minha leitura, quando eu saí pra reclamar, vi que os alunos pareciam assustados.{/color}"
    "{color=#0a0000}Fui para sala e descobri que a Astrid tinha sido assassinada... E aí... Eu...{/color}"
    hide kaito_box
    show padrao_box at left
    "{color=#0a0000}Ele começou a chorar novamente{/color}"
    hide padrao_box
    show kaito_box at left
    "{color=#0a0000}Eu comecei a entrar em pânico e...{/color}"
    hide kaito_box
    hide kaito
    show kaitos at right
    hide marcos
    show marco at left
    show padrao_box at left
    "{color=#0a0000}Marco deu um abraço em Kaito pra acalmar ele.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}Calma, calma, vai passar...{/color}"
    hide marco_box
    hide marco
    show marcos at left
    hide kaitos
    show kaito at right
    show kaito_box at left
    "{color=#0a0000}Mas a Astrid não vai voltar.{/color}"
    hide kaito_box
    hide marcos
    show marco at left
    hide kaito
    show kaitos at right
    show marco_box at left
    "{color=#0a0000}Eu sei, eu também estou me sentindo mal.{/color}"
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Marco olhou para mim após isso{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}Então? Você acha que Kaito é o possível assassino?{/color}"
    hide marco_box
    hide marco
    show marcos at left
    show player_box at left
    "{color=#0a0000}Não. Acho que ele está descartado da lista de suspeitos.{/color}"
    hide player_box
    hide kaitos
    show kaito at right
    show padrao_box at left
    "{color=#0a0000}Kaito me olhou aliviado.{/color}"
    hide padrao_box
    show kaito_box at left
    "{color=#0a0000}Muito obrigado por me compreender. Eu espero que a alma da Olívia e da Astrid descansem em paz e que vocês prendam o assassino.{/color}"
    hide kaito_box
    hide kaito
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Quem é o próximo agora?{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}É o Jacob.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Está certo.{/color}"
    hide marco_box
    hide marco
    show marcos at left
    show padrao_box at left
    "{color=#0a0000}Fomos então até o outro canto da sala onde Jacob estava, ele parecia tenso também e trêmulo.{/color}"
    hide padrao_box
    show jacob at right
    show jacob_box at left
    "{color=#0a0000}Já é a segunda pessoa que morre nessa escola...{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Exatamente! Até agora eu tô perplexo com essa porra.{/color}"
    hide marco_box
    hide jacobs
    show jacob at right
    hide marco
    show marcos at left
    show jacob_box at left    
    "{color=#0a0000}Marco, eu não tô bem não, só de pensar que qualquer hora pode vir alguém me esfaquear, isso me deixa desconfortável.{/color}"
    hide jacob_box
    hide jacob
    show jacobs at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Também estou sentindo o mesmo. Mas [genero] [Nome] tem algo a perguntar para você.{/color}"
    hide marco_box
    hide jacobs
    show jacob at right
    hide marco
    show marcos at left
    show padrao_box at left
    "{color=#0a0000}Jacob levantou a cabeça e olhou para mim.{/color}"
    hide padrao_box
    show jacob_box at left
    "{color=#0a0000}Sim? Pode perguntar, estarei a disposição para responder.{/color}"
    hide jacob_box
    show player_box at left
    "{color=#0a0000}Tudo bem. Eu gostaria de saber se você tinha algum tipo de apatia pela Astrid.{/color}"
    hide player_box
    show jacob_box at left
    "{color=#0a0000}Não vou mentir, eu não ia com a cara dela, mas não era nada além disso. Ela só era chatinha mas nada que me incomodasse de mais.{/color}"
    hide jacob_box
    show player_box at left
    "{color=#0a0000}Ok, bem, você pode me dizer onde você estava quando a Astrid foi assassinada?{/color}"
    hide player_box
    show jacob_box at left
    "{color=#0a0000}Hum, o pior é que eu não me lembro. Eu tenho problemas sérios com memória mas o que vem na minha mente é que eu estava no refeitório pegando água.{/color}"
    "{color=#0a0000}Aí eu acho que depois disso eu fui pra sala de aula e vi esse alvoroço e fiquei desconfortável.{/color}"
    hide jacob_box
    show player_box at left
    "{color=#0a0000}Ok, Jacob. Bem, vou manter você na lista por enquanto, mas saiba que não suspeito mais de você. Quem eu mais suspeito é o Jonathan.{/color}"
    hide player_box
    show jacob_box at left
    "{color=#0a0000}Olha, não sei se foi ele, Jonathan é bem violento, mas sei lá. Porém é bom dar uma olhada.{/color}"
    hide jacob_box
    show player_box at left
    "{color=#0a0000}Está certo, obrigad[genero]!{/color}"
    hide player_box
    hide jacob
    hide marcos
    
    scene corredor1
    play music "Corredor ambientação.mp3"
    show marco
    show marco_box at left
    '{color=#0a0000} Agora é o "bonito" que sobrou. Mas sinceramente eu tenho quase certeza que é o Jonathan.{/color}'
    hide marco_box
    hide marco

    scene escolafeio
    play music "Escola-canto-feio ambientação.mp3"
    show padrao_box at left
    "{color=#0a0000}Fomos para o canto de trás da escola onde Jonathan estava fumando.{/color}"
    hide padrao_box
    show jonathan at right
    show marcos at left
    show jonathan_box at left
    "{color=#0a0000}Tsk nem vem!!! O que vocês querem???{/color}"
    hide jonathan_box
    show player_box at left
    "{color=#0a0000}Jonathan! Precisamos perguntar sobre o assassinato da Astrid, tenta pelo menos se conter.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Jonathan bufou e olhou para nós com ódio.{/color}"
    hide padrao_box
    show jonathan_box at left
    "{color=#0a0000}Olha, eu não matei a Astrid, seus imbecis! Tudo que eu fiz foi fumar aqui atrás escondido pra ficar mais calmo porque aquela vadia estava me traindo na minha frente!{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}O engraçado que você cantou [genero] [Nome] e mais algumas garotas quando você estava em um relacionamento com a Astrid!{/color}"
    hide marco_box
    hide jonathans
    show jonathan at right
    hide marco
    show marcos at left
    show jonathan_box at left
    "{color=#0a0000}E daí? Eu queria mesmo, ela era mais uma diversãozinha pra mim!{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Assim como a Olívia, né? Jonathan, eu entendo o que passou, mas ninguém é objeto.{/color}"
    hide marco_box
    hide jonathans
    show jonathan at right
    hide marco
    show marcos at left
    show padrao_box at left
    "{color=#0a0000}Jonathan parecia querer ir pra cima do Jacob mas se conteve e deu um suspiro.{/color}"
    hide padrao_box
    show jonathan_box at left
    "{color=#0a0000}Você está certo, tsk, me considero uma pessoa infeliz, mandando a real, por mais que eu tente me bancar o durão.{/color}"
    "{color=#0a0000}Por dentro eu tô quebrado, estraçalhado e no fundo eu sei que as merdas que faço não me faz parecer mais forte.{/color}"
    hide jonathan_box
    show padrao_box at left
    "{color=#0a0000}Ele colocou a mão sobre o rosto e olhou para nós um tanto envergonhado de si mesmo.{/color}"
    hide padrao_box
    show jonathan_box at left
    "{color=#0a0000}Agh cara, como eu sou um imbecil de merda!{/color}"
    hide jonathan_box
    show padrao_box at left
    "{color=#0a0000}Ele retirou a mão do rosto e olhou para nós tentando manter a postura.{/color}"
    hide padrao_box
    show jonathan_box at left
    "{color=#0a0000}Mas enfim, eu tava fumando cigarro aqui de boa, é isso.{/color}"
    hide jonathan_box
    show player_box at left
    "{color=#0a0000}Tudo bem. E lembre-se: Nunca é tarde pra você melhorar como pessoa.{/color}"
    hide player_box
    show jonathan_box at left
    "{color=#0a0000}O foda é que eu já tô no buraco.{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}E cada vez que você age desse jeito você se afunda mais! Jonathan, você tá cavando sua própria cova, não consegue reparar isso?{/color}"
    hide marco_box
    hide jonathans
    show jonathan at right
    hide marco
    show marcos at left
    show jonathan_box at left
    "{color=#0a0000}Você não entende o que passei! Diferente de mim, você sempre foi amado pelos seus pais!{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Sim, eu sei. Mas saiba que sempre vai ter alguém do seu lado.{/color}"
    hide marco_box
    hide jonathans
    show jonathan at right
    hide marco
    show marcos at left
    show jonathan_box at left
    "{color=#0a0000}Não... Não vai, agora vaza e me deixa em paz!{/color}"
    hide jonathan_box
    hide jonathan
    show jonathans at right
    hide marcos
    show marco at left
    show marco_box at left
    "{color=#0a0000}Jonathan...{/color}"
    hide marco_box
    hide jonathans
    show jonathan at right
    hide marco
    show marcos at left
    show padrao_box at left
    "{color=#0a0000}Jonathan olhou com ódio para nós e gritou.{/color}"
    hide padrao_box
    show jonathan_box at left
    "{color=#0a0000}VAZA!{/color}"
    hide jonathan_box
    hide jonathan
    hide marcos
    
    scene corredor2
    play music "Corredor dos quartos ambientação.mp3"
    show marco at center
    show marco_box at left
    "{color=#0a0000}Sabe, [Nome], o Jonathan sem dúvidas é o mais propenso a ser o assassino, mas de certa forma eu tenho uma pena dele, até porque ele nunca soube o que é ser amado.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Eu entendo, também acho isso. {/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Preciso te falar uma coisa importante também. Sabe o Jacob? Não aconselho você remover da lista de suspeitos também. As mudanças bruscas de comportamento dele não são a toa não.{/color}"
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Olhei pra ele um pouco surpresa.{/color}"
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Poxa... Por que não me avisou antes?{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Eu achei que você já tinha reparado na ficha.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Mas lá não tem nada assim, a não ser a foto, altura e peso dos suspeitos, mas me diz, o que ele tem?{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Como posso dizer isso? Hum... O Jacob na verdade é duas pessoas. Tipo, ele tem dupla personalidade.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Ah sim, bem, agora parece que algo está fazendo sentido as coisas, mas se for ele, no caso, a outra personalidade dele, como que a gente fazer pra prender ele? Porque o Jacob em si é inocente, já o outro cara não.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Eu costumo chamar o outro de Sandman, porque toda vez que eu ia dormir, ele as vezes aparecia pra me encher o saco pedindo para que eu desse Danone de chocolate pra ele. Mó nada haver.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Realmente... Mas me diz, ele tem algo que pode ligar ao assassinato?{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Não. Ah! Na verdade tem sim, ele tinha um ódio especial por médicos e tanto Olívia como Astrid queriam cursar medicina. Sandman culpa os médicos porque uma vez o médico não conseguiu salvar a mãe dele.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Parece que tudo faz sentido agora... Mas me responda a pergunta, se for ele, pode por favor me dizer como que vamos chegar no Jacob e prender?{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Seria bom levar ele para um médico especializado e afastar? Se for o caso.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Está certo, então vamos coletar provas!{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Marco destrancou o quarto deles e entramos lá.{/color}"
    
    scene quartojacob
    play music "Quarto do Jacob.mp3"
    show player_box at left
    "{color=#0a0000}Quando cheguei, percebi que tinham alguns desenhos na parede no lado da cama do Jacob.{/color}"
    '{color=#0a0000}"Bocatheus"{/color}'
    "{color=#0a0000}Nossa... imagina uma boca e um bigode com cachos finalizados.{/color}"
    "{color=#0a0000}Tá, não era nada de importante.{/color}"
    hide player_box 
    scene quartocama
    show padrao_box at left
    "{color=#0a0000}Marco levantou o colchão da cama de Jacob e olhou surpreso. Ele me entregou alguns papéis.{/color}"
    hide padrao_box at left
    show marco_box at left
    show desenho
    "{color=#0a0000}[Nome] vem cá! Acho que encontrei algumas coisas.{/color}"
    hide desenho
    hide marco_box
    show player_box at left
    "{color=#0a0000}Não acredito...{/color}"
    show marco
    hide player_box
    show padrao_box at left
    '{color=#0a0000}Os papéis parecia algum plano pra matar possíveis médicos "incompetentes".{/color}'
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Nossa, mas que motivação esquisita.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Marco parecia perplexo e um pouco chateado também. Ele parecia estar segurando as lágrimas.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}E de pensar que meu melhor amigo... É o assassino.. Agh. Mas espero...{/color}"
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Ele acaba desabando.{/color}"
    "{color=#0a0000}Eu fui até ele e abracei ele.{/color}"
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Acho que você de longe foi o mais forte aqui, você teve que aguentar toda a ansiedade até agora.{/color}"
    "{color=#0a0000}Ainda mais que seu amigo é o assassino por mais que ele de fato não saiba disso... Marco, vai ficar tudo bem. Você vai poder conversar com ele.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Muito obrigado também por tudo, de verdade. Mesmo Jacob sendo meu amigo, eu compreendo que precisamos proteger as vidas de mais pessoas. Na verdade, até a vida dele...{/color}"
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Ele falou enquanto chorava.{/color}"
    hide padrao_box
    show player_box at left
    "{color=#0a0000}Vou esperar você se acalmar um pouco pra resolver o assunto.{/color}"
    hide player_box
    show marco_box at left
    "{color=#0a0000}Está bem.{/color}"
    hide marco_box
    show padrao_box at left
    "{color=#0a0000}Depois de um tempo, Marco se acalmou.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Está pronto?{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Marco suspirou e disse.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}Sim.{/color}"
    hide marco_box
    hide marco
    scene escolafora
    play music "Escola-fora ambientação.mp3"
    show padrao_box at left
    '{color=#0a0000}Fomos até à polícia e mostramos a provas para a polícia e Jacob foi encaminhado para um hospital para poder ficar afastado e conseguir controlar o "Sandman".{/color}'
    "{color=#0a0000}Jacob ficou chocado e chateadíssimo mas no fim ele concordou em ir para o hospital.{/color}"
    "{color=#0a0000}Após isso, Marco parecia abalado, porém compreendeu a situação. Finalmente eu havia finalizado o caso.{/color}"
    "{color=#0a0000}Jonathan começou a tentar controlar os nervos dele e se aproximar mais das outras pessoas de forma saudável.{/color}"
    "{color=#0a0000}E sobre mim, bem, finalmente acabei de finalizar a missão e assim, subir de cargo e honrar a morte de Olívia e de Astrid.{/color}"
    hide padrao_box
    show marco at left
    show player_box at left
    "{color=#0a0000}Então, esse é o fim da missão. Mas realmente tenho uma imensa consideração por vocês.{/color}"
    hide player_box
    show padrao_box at left
    "{color=#0a0000}Marco veio até mim e entregou uma lista de telefones.{/color}"
    hide padrao_box
    show marco_box at left
    "{color=#0a0000}Aqui, para manter contato conosco!  Obrigado por tudo... Ah, aqui está também o telefone da clínica que o Jacob está.{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Obrigado! Vou manter contato sim.{/color}"
    hide player_box
    show camila at right
    hide marco
    show marcos at left
    show camila_box at left
    "{color=#0a0000}Foi mal eu ter surtado contigo aquela hora, mas agora eu te entendo, meu bem. Ah! Espero que não se esqueça de mim.{/color}"
    hide camila_box
    show player_box at left
    "{color=#0a0000}Impossível eu me esquecer de ti, Camila.{/color}"
    hide player_box
    hide camila
    show camilas at right
    show kaito at center
    show kaito_box at left
    "{color=#0a0000}Te desejo em sorte, espero que consiga se tornar [um] ótim[genero] detetive, mais do que já é.{/color}"
    hide kaito_box
    show player_box at left
    "{color=#0a0000}E você um cara bem sucedido! Você consegue!{/color}"
    hide player_box
    show kaito_box at left
    "{color=#0a0000}Obrigado!{/color}"
    hide kaito_box
    hide kaito
    show kaitos at center
    show marco_box at left
    "{color=#0a0000}Bem, então isso é um adeus?{/color}"
    hide marco_box
    show player_box at left
    "{color=#0a0000}Quem sabe a gente possa se ver outro dia? Isso nunca será um adeus.{/color}"
    hide player_box
    hide kaitos
    show kaito at center
    hide camilas
    show camila at right
    show padrao_box at left
    "{color=#0a0000}Eu saí de lá e todos se despediram.{/color}"
    scene telafim
    "{color=#0a0000} {/color}"
    scene creditos
    "{color=#0a0000} {/color}"
    return

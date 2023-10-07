from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Django_Evaluacion_1/index.html')

def user(request):
    data = {"usuario": "ASDFGHJ",
            "nombre": "Guido",
            "apellido_pat": "Álvarez",
            "apellido_mat": "Aqueveque",
            "fecha_nac": "16-05-1987",
            "edad": "37 años",
            "correo_elec": "g.alvarezaqueve.87@gmail.com",
            "ciudad": "Temuco",
    }
    return render(request, 'Django_Evaluacion_1/user.html', data)

def shonen(request):
    data = {"titulo":"Shonen",
            "producto1": "Fullmetal Alchemist",
            "producto2": "One Piece",
            "producto3": "Dragon Ball Z",
            "foto1": "FMA.jpg",
            "foto2": "OP.jpg",
            "foto3": "DBZ.jpg",
            }
    return render(request, 'Django_Evaluacion_1/productos.html', data)

def seinen(request):
    data = {"titulo":"Seinen",
            "producto1": "Berserk",
            "producto2": "Vagabond",
            "producto3": "Vinland Saga",
            "foto1": "BER.jpg",
            "foto2": "VAG.jpg",
            "foto3": "VL.jpg",
            }
    return render(request, 'Django_Evaluacion_1/productos.html', data)

def shojo(request):
    data = {"titulo":"Shojo",
            "producto1": "Sailor Moon",
            "producto2": "Banana Fish",
            "producto3": "Orange",
            "foto1": "SM.jpg",
            "foto2": "BF.jpg",
            "foto3": "OR.jpg",
            }
    return render(request, 'Django_Evaluacion_1/productos.html', data)


def descripcion(request):    #Faltó incluir las descripciones de productos
    data_desc = { 
        "Shonen": {
            "Fullmetal Alchemist": """Tras la muerte de su madre cuando eran apenas unos niños, 
            Edward y Alphonse Elric, decidieron dedicar su vida a obtener todos 
            los conocimientos posibles sobre alquimia que les permitieran traer de 
            vuelta a la vida a su madre. Cuando se creían preparados, llevaron a cabo 
            un peligroso y prohibido ritual alquímico que se tuerce con desastrosas 
            consecuencias; la pérdida de una pierna por parte de Edward y la desaparición 
            de Alphonse. Al coste de su brazo, Edward consigue recuperar el alma de su 
            hermano uniéndola a una armadura.""", 
            
            "One Piece": """One Piece narra la historia de un joven llamado Monkey D. Luffy, 
            que inspirado por su amigo pirata Shanks, comienza un viaje para 
            alcanzar su sueño, ser el Rey de los piratas, para lo cual deberá 
            encontrar el tesoro One Piece dejado por el anterior rey de los piratas 
            Gol D. Roger.""",

            "Dragon ball Z": """Su trama describe las aventuras de Goku, un guerrero saiyajin, cuyo fin 
            es proteger a la Tierra de otros seres que quieren conquistarla y exterminar a 
            la humanidad. Conforme transcurre la trama, conoce a otros personajes que le ayudan 
            en este propósito."""},

        "Seinen": {
            "Berserk": """Berserk nos cuenta la historia de Guts, un antihéroe mercenario que vaga por 
            el mundo en solitario en búsqueda de Apóstoles, unos seres demoníacos que antaño 
            fueron humanos pero que sacrificaron una parte importante de sus vidas para 
            conseguir poderes que les permitieran alcanzar sus más oscuros deseos.""",

            "Vagabond": """Se trata de un relato biográfico de la vida legendario espadachín Miyamoto 
            Musashi (1584-1645), la figura histórica más importante de Japón en lo que se 
            refiere al desarrollo de las técnicas de luchas con espada (por ejemplo, fundó 
            l estiloNiten Ichi de combate con espadas, en el que se emplean simultaneamente 
            una espada larga -en la mano derecha- y una espada corta -en la mano izquierda-) 
            y autor del libro de estrategia El libro de los cinco anillos. La leyenda cuenta 
            que a los trece años mató a su primer contrincante en duelo, y antes de cumplir 
            los treinta años ya había salido victorioso de 60 duelos.""",

            "Vinland Saga": """Vinland Saga nos sitúa en el siglo XI, cuando Dinamarca e Inglaterra 
            se encontraban en guerra, con los vikingos amenazando con apoderarse por completo de la isla británica.
            En este contexto, un joven llamado Thorfinn busca vengarse del hombre que asesinó a su padre, Askelaad, 
            un vikingo y mercenario inteligente y peligroso. Lo interesante es que los eventos llevan a Thorfinn a 
            volverse una especie de protegido de Askelaad, a pesar de que este está plenamente consciente de las intenciones 
            de Thorfinn, quien no solo no las esconde, sino que constantemente reta a Askelaad a duelos a muerte a lo 
            largo de los años; duelos que Askelaad siempre gana.
            Thorfinn, aunque no está muy interesado en aquello que no tenga que ver con su venganza, se verá inmiscuido 
            en problemas de gran envergadura que terminarán por marcar un camino inesperado y lleno de peligros para él."""},

        "Shojo": {
            "Sailor Moon": """Sailor Moon nos cuenta la historia de esta estudiante atolondrada, holgazana 
            y que prefiere mil veces perseguir al chico guapo de turno o jugar a los videojuegos 
            antes que ponerse a estudiar. Su vida cambiará cuando reciba la visita de Luna, 
            una gata parlante que en seguida le revela su misión: Ella es Sailor Moon, la 
            guerrera guardiana de la luna destinada a luchar contra el mal. Le cuenta que 
            está buscando a su princesa, la soberana del reino de la Luna Serenity y por ende, 
            al cristal de plata que debe de llevar consigo que les ayudará a reconstruir su reino.""",

            "Banana Fish": """Aslan Jade Callenreese, conocido como Ash Lynx, es un habilidoso y atractivo jefe 
            de pandilla de 17 años que controla una zona de New York bajo el mando del depravado 
            capo mafioso, Golzine Dino, quien lo tiene bajo su poder y abusa sexualmente de él 
            desde niño. Un día ocurre un inusual incidente en el territorio de Ash que deja tras 
            de sí las palabras claves “Banana Fish” y una extraña sustancia desconocida. Por otro 
            lado, los japoneses Shunichi Ibe; camarógrafo profesional, y Okumura Eiji; asistente 
            de Ibe, viajan a New York para realizar un reportaje sobre pandillas bajo la protección 
            del Departamento de Policías de New York, quienes paralelamente se encuentran trabajando 
            en una “epidemia” de extraños suicidios que conectan con la mafia de Golzine. Poco 
            después de la llegada de los japoneses a New York ocurre un repentino enfrentamiento 
            entre pandillas a raíz de la sustancia desconocida que resguardó Ash. Eiji y Ibe se 
            ven involucrados en los sucesos. Posteriormente será el deseo de Eiji sumarse a la 
            peligrosa travesía del salvaje Ash Lynx quien, por motivos personales, está en busca de 
            lo que podría ser una persona con nombre clave “Banana Fish”.""",

            "Orange":"""El primer día de clase, Naho, una chica de 16 años, recibe una misteriosa carta 
            de quien dice ser su yo del futuro, en la que se predice de forma exacta cada cosa que 
            está a punto de pasarle. Además, la remitente le aconseja no llevar a cabo determinadas 
            acciones. Haciendo caso omiso de ella, Naho invita al chico nuevo que acaba de llegar 
            desde Tokio, Kakeru, a salir con sus amigos después del instituto. Pero algo terrible 
            le ocurre a Kakeru ese día. Algo que podría no haber sucedido si hubiera vuelto antes 
            a casa. Sabiéndolo, Naho decide comenzar a seguir las instrucciones. Aunque hacer frente 
            al presente sin dejar lugar para el arrepentimiento no resulta tan sencillo como debiera."""}
    }   

    # descripcion =  data_desc.get(categoria, {}).get(producto, "descripcion no se encuentra")
    
    # data = {"titulo": "descripcion",
    #        "categoria": categoria,
    #        "producto": producto,
    #        "descripcion": descripcion
    #}

    return render(request, 'Django_Evaluacion_1/descripcion.html', data_desc)
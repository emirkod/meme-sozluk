while True :
            meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap(lots of laugh)",
            "NİCE TRY":"İyi denemeydi",
            "EZ WİN": "Kolaydı",
            "SIGMA BOY": "ciddi,umursamaz,havalı erkek",
            "TROLL FACE": "trollemeyi,başkasını sinirlendirmeyi veya şaka yaptığını belirtmek için kullanılır.",
            "ME GUSTA": "rahatsız edici ama hoşuma gidiyor demektir.",
            "Y U NO GUY": "Birşeyin neden mantıklı olmadığını söylemek için kullanılır."
            }
            word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
            if word in meme_dict.keys():
                print(meme_dict[word])
            else:
                print("Henüz benim sözlüğümde bu kelime yok.")

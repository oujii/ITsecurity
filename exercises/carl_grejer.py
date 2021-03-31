bio_filmer = {"The Green Book": "20.00",
              "Grinchen": "19.00",
              "Borta med vinden": "22.00"
              }

print("Dessa filmer visas:")
for key in bio_filmer:
    print(key)

film = input("Vilken film vill du se?\n")

bio_tid = bio_filmer.get(film)
if bio_tid == None:
    print("Den går inte nu")
else:
    print(film, "går kl ", bio_tid)

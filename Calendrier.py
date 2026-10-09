#cc
import calendar

print('Choisie ton année :')
annee = input()
annee = int(annee)

print('Choisie ton mois :')
mois = input()
mois = int(mois)

print('Choisie ton jour :')
jour = input()
jour = int(jour)
                                                                                                                retourj = (calendar.weekday(annee,mois,jour))
                                                                                                                retourj = str(retourj)

match retourj:
                case "0":
                        print('lundi')
                case "1":
                        print('mardi')
                case "2":
                        print('mercredi')
                case "3":
                        print('jeudi')
                case "4":
                        print('vendredi')
                case "5":
                        print('samedi')
                case "6":
                        print('dimanche')
                case _:
                        print('erreur')

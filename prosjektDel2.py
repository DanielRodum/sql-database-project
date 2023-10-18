import sqlite3
import re
import datetime

con = sqlite3.connect("ProsjektDB.db")
cursor = con.cursor()


def pre():

    #Oppgave a)

    cursor.execute("""INSERT INTO Jernbanestasjon (Navn, Hoyde) VALUES 
                        ('Bodø', 4.1), 
                        ('Fauske', 34.0), 
                        ('Mo i Rana', 3.5), 
                        ('Mosjøen', 6.8), 
                        ('Steinkjer', 3.6), 
                        ('Trondheim', 5.1)""")

    cursor.execute("""INSERT INTO Banestrekning (Navn, Fremdriftsenergi, B_Startstasjon, B_Endestasjon) VALUES 
                        ('Nordlandsbanen', 'Diesel', 'Trondheim', 'Bodø')""")

    cursor.execute("""INSERT INTO B_Mellomstasjon (Mellomstasjon_Navn, Banestrekning_Navn) VALUES 
                        ('Steinkjer', 'Nordlandsbanen'), 
                        ('Mosjøen', 'Nordlandsbanen'), 
                        ('Mo i Rana', 'Nordlandsbanen'), 
                        ('Fauske', 'Nordlandsbanen')""")

    cursor.execute("""INSERT INTO Delstrekning (Lengde, Sportype, Banestrekning_Navn, StasjonEn, StasjonTo) VALUES 
                        (120, 'Dobbeltspor', 'Nordlandsbanen', 'Trondheim', 'Steinkjer'),
                        (280, 'Enkeltspor', 'Nordlandsbanen', 'Steinkjer', 'Mosjøen'),
                        (90, 'Enkeltspor', 'Nordlandsbanen', 'Mosjøen', 'Mo i Rana'),
                        (170, 'Enkeltspor', 'Nordlandsbanen', 'Mo i Rana', 'Fauske'),
                        (60, 'Enkeltspor', 'Nordlandsbanen', 'Fauske', 'Bodø')
                        """)


    #Oppgave b)

    cursor.execute("""INSERT INTO Kunderegister (RegisterID) VALUES (1)""")

    cursor.execute("""INSERT INTO Operator (Navn, Kunderegister) VALUES ('SJ', 1)""")
    
    
    cursor.execute("""INSERT INTO Vognoppsett (OppsettID) VALUES
                        (1),
                        (2),
                        (3)""")
    
    
    cursor.execute("""INSERT INTO Sittevogn (Navn, Operator_Navn) VALUES
                        ('SJ-sittevogn-1', 'SJ'),
                        ('SJ-sittevogn-1', 'SJ'),
                        ('SJ-sittevogn-1', 'SJ'),
                        ('SJ-sittevogn-1', 'SJ')
                        """)
    
    
    cursor.execute("""INSERT INTO Rad (Radnummer, SittevognID) VALUES
                        (1, '1'),
                        (2, '1'),
                        (3, '1'),
                        (1, '2'),
                        (2, '2'),
                        (3, '2'),
                        (1, '3'),
                        (2, '3'),
                        (3, '3'),
                        (1, '4'),
                        (2, '4'),
                        (3, '4')""")
                        
    cursor.execute("""INSERT INTO Sitteplass (Setenummer, SittevognID, Radnummer) VALUES
                        (1, 1, 1),
                        (2, 1, 1),
                        (3, 1, 1),
                        (4, 1, 1),
                        (5, 1, 2),
                        (6, 1, 2),
                        (7, 1, 2),
                        (8, 1, 2),
                        (9, 1, 3),
                        (10, 1, 3),
                        (11, 1, 3),
                        (12, 1, 3),
                        (1, 2, 1),
                        (2, 2, 1),
                        (3, 2, 1),
                        (4, 2, 1),
                        (5, 2, 2),
                        (6, 2, 2),
                        (7, 2, 2),
                        (8, 2, 2),
                        (9, 2, 3),
                        (10, 2, 3),
                        (11, 2, 3),
                        (12, 2, 3),
                        (1, 3, 1),
                        (2, 3, 1),
                        (3, 3, 1),
                        (4, 3, 1),
                        (5, 3, 2),
                        (6, 3, 2),
                        (7, 3, 2),
                        (8, 3, 2),
                        (9, 3, 3),
                        (10, 3, 3),
                        (11, 3, 3),
                        (12, 3, 3),
                        (1, 4, 1),
                        (2, 4, 1),
                        (3, 4, 1),
                        (4, 4, 1),
                        (5, 4, 2),
                        (6, 4, 2),
                        (7, 4, 2),
                        (8, 4, 2),
                        (9, 4, 3),
                        (10, 4, 3),
                        (11, 4, 3),
                        (12, 4, 3)
                        """)                    
                        

    cursor.execute("""INSERT INTO Sovevogn (Navn, Operator_Navn) VALUES
                        ('SJ-sovevogn-1', 'SJ')""")
    
    cursor.execute("""INSERT INTO Sovekupe (Kupenummer, SovevognID) VALUES
                        (1, 1),
                        (2, 1),
                        (3, 1),
                        (4, 1)""")
    
    cursor.execute("""INSERT INTO Seng (Sengnummer, SovevognID, Kupenummer) VALUES
                        (1, 1, 1),
                        (2, 1, 1),
                        (3, 1, 2),
                        (4, 1, 2),
                        (5, 1, 3),
                        (6, 1, 3),
                        (7, 1, 4),
                        (8, 1, 4)""")

    cursor.execute("""INSERT INTO SittevognTilVognoppsett (SittevognID, OppsettID, VognNummer) VALUES
                        (1, 1, 1),
                        (2, 1, 2),
                        (3, 2, 1),
                        (4, 3, 1)""")
    
    cursor.execute("""INSERT INTO SovevognTilVognoppsett (SovevognID, OppsettID, VognNummer) VALUES
                        (1, 2, 2)""")
    
    

    cursor.execute("""INSERT INTO Togrute (Operator_Navn, Banestrekning_Navn, Retning, OppsettID) VALUES
                        ('SJ', 'Nordlandsbanen', 'Med', 1),
                        ('SJ', 'Nordlandsbanen', 'Med', 2),
                        ('SJ', 'Nordlandsbanen', 'Mot', 3)""")
    
    cursor.execute("""INSERT INTO RuteTabell_Instans (TogruteID, StasjonsNavn, Ukedag, AnkomstTid, AvgangsTid) VALUES
                        (1, 'Trondheim', 'Mandag', NULL, '07:49'),
                        (1, 'Steinkjer', 'Mandag', '09:51', '09:51'),
                        (1, 'Mosjøen', 'Mandag', '13:20', '13:20'),
                        (1, 'Mo i Rana', 'Mandag', '14:31', '14:31'),
                        (1, 'Fauske', 'Mandag', '16:49', '16:49'),
                        (1, 'Bodø', 'Mandag', '17:34', NULL),

                        (1, 'Trondheim', 'Tirsdag', NULL, '07:49'),
                        (1, 'Steinkjer', 'Tirsdag', '09:51', '09:51'),
                        (1, 'Mosjøen', 'Tirsdag', '13:20', '13:20'),
                        (1, 'Mo i Rana', 'Tirsdag', '14:31', '14:31'),
                        (1, 'Fauske', 'Tirsdag', '16:49', '16:49'),
                        (1, 'Bodø', 'Tirsdag', '17:34', NULL),

                        (1, 'Trondheim', 'Onsdag', NULL, '07:49'),
                        (1, 'Steinkjer', 'Onsdag', '09:51', '09:51'),
                        (1, 'Mosjøen', 'Onsdag', '13:20', '13:20'),
                        (1, 'Mo i Rana', 'Onsdag', '14:31', '14:31'),
                        (1, 'Fauske', 'Onsdag', '16:49', '16:49'),
                        (1, 'Bodø', 'Onsdag', '17:34', NULL),

                        (1, 'Trondheim', 'Torsdag', NULL, '07:49'),
                        (1, 'Steinkjer', 'Torsdag', '09:51', '09:51'),
                        (1, 'Mosjøen', 'Torsdag', '13:20', '13:20'),
                        (1, 'Mo i Rana', 'Torsdag', '14:31', '14:31'),
                        (1, 'Fauske', 'Torsdag', '16:49', '16:49'),
                        (1, 'Bodø', 'Torsdag', '17:34', NULL),

                        (1, 'Trondheim', 'Fredag', NULL, '07:49'),
                        (1, 'Steinkjer', 'Fredag', '09:51', '09:51'),
                        (1, 'Mosjøen', 'Fredag', '13:20', '13:20'),
                        (1, 'Mo i Rana', 'Fredag', '14:31', '14:31'),
                        (1, 'Fauske', 'Fredag', '16:49', '16:49'),
                        (1, 'Bodø', 'Fredag', '17:34', NULL),

                        (2, 'Trondheim', 'Alle dager', NULL, '23:05'),
                        (2, 'Steinkjer', 'Alle dager', '00:57', '00:57'),
                        (2, 'Mosjøen', 'Alle dager', '04:41', '04:41'),
                        (2, 'Mo i Rana', 'Alle dager', '05:55', '05:55'),
                        (2, 'Fauske', 'Alle dager', '08:19', '08:19'),
                        (2, 'Bodø', 'Alle dager', '09:05', NULL),

                        (3, 'Mo i Rana', 'Mandag', NULL, '08:11'),
                        (3, 'Mosjøen', 'Mandag', '09:14', '09:14'),
                        (3, 'Steinkjer', 'Mandag', '12:31', '12:31'),
                        (3, 'Trondheim', 'Mandag', '14:13', NULL),

                        (3, 'Mo i Rana', 'Tirsdag', NULL, '08:11'),
                        (3, 'Mosjøen', 'Tirsdag', '09:14', '09:14'),
                        (3, 'Steinkjer', 'Tirsdag', '12:31', '12:31'),
                        (3, 'Trondheim', 'Tirsdag', '14:13', NULL),

                        (3, 'Mo i Rana', 'Onsdag', NULL, '08:11'),
                        (3, 'Mosjøen', 'Onsdag', '09:14', '09:14'),
                        (3, 'Steinkjer', 'Onsdag', '12:31', '12:31'),
                        (3, 'Trondheim', 'Onsdag', '14:13', NULL),

                        (3, 'Mo i Rana', 'Torsdag', NULL, '08:11'),
                        (3, 'Mosjøen', 'Torsdag', '09:14', '09:14'),
                        (3, 'Steinkjer', 'Torsdag', '12:31', '12:31'),
                        (3, 'Trondheim', 'Torsdag', '14:13', NULL),

                        (3, 'Mo i Rana', 'Fredag', NULL, '08:11'),
                        (3, 'Mosjøen', 'Fredag', '09:14', '09:14'),
                        (3, 'Steinkjer', 'Fredag', '12:31', '12:31'),
                        (3, 'Trondheim', 'Fredag', '14:13', NULL)""")
    
    cursor.execute("""INSERT INTO Kunde (Navn, Epost, Mobilnummer, RegisterID) VALUES
                        ('Petter Smart', 'pettersmart@gmail.com', 47826743, 1),
                        ('Skrue McDuck', 'rikesteiverden@duckmail.com', 12345678, 1)""")
    
    cursor.execute("""INSERT INTO Kundeordre (Dato, Tid, Antall, Kundenummer) VALUES
                        ('26.03.2023', '23:59', 1, 1),
                        ('03.04.2023', '23:59', 1, 1),
                        ('03.04.2023', '23:59', 2, 1)""")

    cursor.execute("""INSERT INTO SeteBillett (Ordrenummer, ForekomstID, Dato, Setenummer, SittevognID) VALUES
                        (1, 1, "03.04.2023", 11, 1),
                        (2, 1, "03.04.2023", 12, 1),
                        (3, 2, "03.04.2023", 8, 3)""")

    cursor.execute("""INSERT INTO SeteBillett_StartEllerSlutt (BillettID, TogruteID, StasjonsNavn, Ukedag) VALUES
                        (1, 1, "Trondheim", "Mandag"),
                        (1, 1, "Fauske", "Mandag"),
                        (2, 1, "Trondheim", "Mandag"),
                        (2, 1, "Bodø", "Mandag"),
                        (3, 2, "Steinkjer", "Mandag"),
                        (3, 2, "Mo i Rana", "Mandag")""")
    
    cursor.execute("""INSERT INTO SengBillett (Ordrenummer, ForekomstID, Dato, Sengnummer, SovevognID) VALUES
                        (3, 2, "03.04.2023", 5, 1)""")
    
    cursor.execute("""INSERT INTO SengBillett_StartEllerSlutt (BillettID, TogruteID, StasjonsNavn, Ukedag) VALUES
                        (1, 2, "Steinkjer", "Mandag"),
                        (1, 2, "Mo i Rana", "Mandag")""")
        

    #Oppgave f)

    cursor.execute("""INSERT INTO Togruteforekomst (ForekomstID, Dato, TogruteID) VALUES
                        (1, '03.04.2023', 1),
                        (2, '03.04.2023', 2),
                        (3, '03.04.2023', 3),
                        (4, '04.04.2023', 1),
                        (5, '04.04.2023', 2),
                        (6, '04.04.2023', 3)""")
    


#Oppgave c)

def OppgaveC():
    cursor.execute("SELECT Navn FROM Jernbanestasjon")
    stasjoner_raw = cursor.fetchall()
    stasjoner = []
    for i in range (0, len(stasjoner_raw)):
        stasjoner.append(stasjoner_raw[i][0])
    while True:
        print(stasjoner)
        Stasjon = input(f"\nHvilken stasjon ønsker du å reise fra? (Skriv tall fra 1 til {len(stasjoner)}) ")
        if (Stasjon.isdigit() == False) or (int(Stasjon)-1 < 0) or (int(Stasjon)-1 >= len(stasjoner)):
            print("Ikke gyldig stasjon. Velg en ny fra listen\n")
        else:
            break
    while True:
        Ukedag = input(f"Hvilken ukedag ønsker du å reise fra {stasjoner[int(Stasjon)-1]}? ")
        if Ukedag.lower() not in ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]:
            print("Ikke gyldig ukedag. Prøv igjen\n")
        else:
            break
    Ukedag_inn = Ukedag[0].upper()+Ukedag[1:].lower()
    cursor.execute("""  SELECT Togrute.TogruteID, Togrute.Retning
                        FROM (Rutetabell_Instans JOIN Togrute ON Rutetabell_Instans.TogruteID = Togrute.TogruteID)
                        WHERE Stasjonsnavn = ? AND (Ukedag = ? OR Ukedag = 'Alle dager')""", (stasjoner[int(Stasjon)-1], Ukedag_inn))
    Resultat = cursor.fetchall()
    print()
    for i in Resultat:
        if i[1] == "Med":
            print(f"Togrute: {i[0]} | Retning: Trondheim - Bodø")
        else:
            print(f"Togrute: {i[0]} | Retning: Mo i Rana - Trondheim")
    print()


#Oppgave d)

def OppgaveD():

    cursor.execute("SELECT Navn FROM Jernbanestasjon")
    stasjoner_raw = cursor.fetchall()
    stasjoner = []
    for i in range (0, len(stasjoner_raw)):
        stasjoner.append(stasjoner_raw[i][0])
        
    while True:
        print(stasjoner)
        Startstasjon = input(f"Hvilken stasjon ønsker du å reise fra? (Skriv tall fra 1 til {len(stasjoner)}) ")
        if (Startstasjon.isdigit() == False) or (int(Startstasjon)-1 < 0) or (int(Startstasjon)-1 >= len(stasjoner)):
            print("Ikke gyldig stasjon. Velg en ny fra listen")
        elif Startstasjon.lower() == "exit":
            return None
        else:
            break

    while True:
        print(stasjoner)
        Sluttstasjon = input(f"Hvilken stasjon ønsker du å reise til? (Skriv tall fra 1 til {len(stasjoner)}) ")
        if (Sluttstasjon.isdigit() == False) or (int(Sluttstasjon)-1 < 0) or (int(Sluttstasjon)-1 >= len(stasjoner)):
            print("Ikke gyldig stasjon. Velg en ny fra listen")
        elif Sluttstasjon.lower() == "exit":
            return None
        else:
            break
    
    if Sluttstasjon < Startstasjon:
        retning = "Med"
    else:
        retning = "Mot"

    while True:
        Dato1 = input("Skriv inn ønsket reisedato ")
        Dag1 = int(Dato1.split(".")[0])
        Måned1 = int(Dato1.split(".")[1])
        År1 = int(Dato1.split(".")[2])
        p = r'^([0-2]?[0-9]|3[0-1])\.([0]?[0-9]|1[0-2])\.[0-9]{4}$'
        if re.match(p, Dato1):
            if Dag1 < 10 or Måned1 < 10:
                if Dag1 < 10 and not Måned1 < 10:
                    Dato1 = "0" + str(Dag1) + "." + str(Måned1) + "." + str(År1)
                elif Måned1 < 10 and not Dag1 < 10:
                    Dato1 = str(Dag1) + ".0" + str(Måned1) + "." + str(År1)
                else:
                    Dato1 = "0" + str(Dag1) + ".0" + str(Måned1) + "." + str(År1)
            if Dag1 == 31:
                if Måned1 == 12:
                    Dato2 = "01.01." + str(År1+1)
                elif Måned1 >= 10:
                    Dato2 = "01." + str(Måned1+1) + "." + str(År1)
                else:
                    Dato2 = "01.0" + str(Måned1+1) + "." + str(År1)
            else:
                if Dag1 < 9:
                    Dato2 = "0" + str(Dag1+1) + "." + Dato1.split(".")[1] + "." + str(År1)
                else:
                    Dato2 = str(Dag1+1) + "." + Dato1.split(".")[1] + "." + str(År1)
            break
        else:
            print("Ikke gyldig dato. Prøv igjen ")
    
    while True:
        Klokkeslett = input("Skriv inn ønsket klokkeslett ")
        p = r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
        if re.match(p, Klokkeslett):
            break
        else:
            print("Ikke gyldig klokkeslett. Prøv igjen ")

    cursor.execute("""  SELECT DISTINCT *
                        FROM (Togrute INNER JOIN (Togruteforekomst INNER JOIN ( (SELECT * FROM Rutetabell_Instans WHERE Stasjonsnavn =:Startstasjon OR AnkomstTid is null) AS RTI1 INNER JOIN 
                                                        (SELECT * FROM Rutetabell_Instans WHERE Stasjonsnavn =:Sluttstasjon) AS RTI2 
                                                        ON RTI1.TogruteID = RTI2.TogruteID ) AS RTI3
                                                        ON Togruteforekomst.TogruteID = RTI3.TogruteID )  AS Ruteforekomster ON Togrute.TogruteID = Ruteforekomster.TogruteID )
                        WHERE (Dato =:Dato1 AND Togrute.Retning =:retning) OR (Dato =:Dato2 AND Togrute.Retning =:retning) """, {"Startstasjon":stasjoner[int(Startstasjon)-1], "Klokkeslett":Klokkeslett, "Sluttstasjon":stasjoner[int(Sluttstasjon)-1], "Dato1":Dato1, "Dato2":Dato2, "retning":retning})
    mellomliste = []    
    result = cursor.fetchall()
    for res in result:
        reslist = []
        if res[7] or res[11] == None:
            None
        elif (res[6] == Dato1 and res[11] == None and res[12] > res[16]):
            reslist.append(res[5])
            mellomliste.append(tuple(reslist))
    
    cursor.execute("""  SELECT DISTINCT ForekomstID
                        FROM (Togrute INNER JOIN (Togruteforekomst INNER JOIN ( (SELECT * FROM Rutetabell_Instans WHERE Stasjonsnavn =:Startstasjon) AS RTI1 INNER JOIN 
                                                        (SELECT * FROM Rutetabell_Instans WHERE Stasjonsnavn =:Sluttstasjon) AS RTI2 
                                                        ON RTI1.TogruteID = RTI2.TogruteID ) AS RTI3
                                                        ON Togruteforekomst.TogruteID = RTI3.TogruteID ) AS Ruteforekomster ON Togrute.TogruteID = Ruteforekomster.TogruteID ) 
                        WHERE (Dato =:Dato1 AND Ruteforekomster.AvgangsTid >=:Klokkeslett AND Togrute.Retning =:retning )  OR (Dato =:Dato2 AND Togrute.Retning =:retning)  """, {"Startstasjon":stasjoner[int(Startstasjon)-1], "Klokkeslett":Klokkeslett, "Sluttstasjon":stasjoner[int(Sluttstasjon)-1], "Dato1":Dato1, "Dato2":Dato2, "retning":retning })
    
    result = cursor.fetchall()
    for togruteID in mellomliste:
        if not togruteID in result:
            result = result + mellomliste
    utliste = []
    for i in range(len(result)):
        utliste.append(result[i][0])
    for i in range(len(utliste)):
        cursor.execute( """ SELECT DISTINCT *
                        FROM (Togrute INNER JOIN (Togruteforekomst INNER JOIN ( (SELECT * FROM Rutetabell_Instans WHERE Stasjonsnavn =:Startstasjon) AS RTI1 INNER JOIN 
                                                        (SELECT * FROM Rutetabell_Instans WHERE Stasjonsnavn =:Sluttstasjon) AS RTI2 
                                                        ON RTI1.TogruteID = RTI2.TogruteID ) AS RTI3
                                                        ON Togruteforekomst.TogruteID = RTI3.TogruteID ) AS Ruteforekomster ON Togrute.TogruteID = Ruteforekomster.TogruteID ) 
                        WHERE ((Dato =:Dato1 AND Ruteforekomster.AvgangsTid >=:Klokkeslett AND Togrute.Retning =:retning )  OR (Dato =:Dato2 AND Togrute.Retning =:retning)) AND Togruteforekomst.ForekomstID =:ID """, {"Startstasjon":stasjoner[int(Startstasjon)-1], "Klokkeslett":Klokkeslett, "Sluttstasjon":stasjoner[int(Sluttstasjon)-1], "Dato1":Dato1, "Dato2":Dato2, "retning":retning, "ID":utliste[i]})
        RuteInfo = cursor.fetchall()
        print(f"ForekomstID: {utliste[i]} Startstasjon: {stasjoner[int(Startstasjon)-1]} Avgangstid: {RuteInfo[0][12]} Endestasjon: {stasjoner[int(Sluttstasjon)-1]}  Ankomsttid: {RuteInfo[0][16]} Dato: {RuteInfo[0][6]}")

    return [utliste, stasjoner[int(Startstasjon)-1], stasjoner[int(Sluttstasjon)-1]]


#Oppgave e)

def OppgaveE():
    navn = input("Hva er navnet ditt? ")
    while True:
        epost = input("Hva er epost-addressen din? ")
        if "@" not in epost:
            print("Dette er ikke en gyldig epost-addresse. Prøv igjen ")
        else:
            break
    while True:
        mobil = input("Hva er mobilnummeret ditt? (Må være nummer fra Norge) ")
        if mobil.isdigit() == False or len(mobil) != 8:
            print("Dette er ikke et gyldig norsk nummer. Prøv igjen ")
        else:
            break
    cursor.execute("""INSERT INTO Kunde (Navn, Epost, Mobilnummer, RegisterID) VALUES
                        ('Petter Smart', 'pettersmart@gmail.com', 47826743, 1),
                        ('Skrue McDuck', 'rikesteiverden@duckmail.com', 12345678, 1),
                        (?, ?, ?, 1)""", (navn, epost, int(mobil)))
    vis = input("Vil du se brukerne i kunderegisteret? (ja/nei) ").lower()
    if vis == "ja":
        cursor.execute("SELECT * FROM Kunde")
        print(cursor.fetchall())


#Oppgave g)

def OppgaveG():
    while True:
        reg = input("Har du registrert bruker? (J/N) ").lower()
        if reg == "n":
            conf = input("Vil du lage en bruker? (J/N) ").lower()
            if conf == "j":
                OppgaveE()
            else:
                print("Takk for ingenting ")
                return None
        elif reg == "j":

            cursor.execute("SELECT Kundenummer FROM Kunde")
            kundenr_raw = cursor.fetchall()
            kundenr = []
            for i in range (0, len(kundenr_raw)):
                kundenr.append(kundenr_raw[i][0])
            while True:
                knr = input("Hva er ditt kundenummer? ")
                if knr.lower() == "exit":
                    return None
                elif knr.isdigit() == False:
                    print("Ikke gyldig kundenummer. Prøv igjen eller skriv EXIT for å avslutte ")
                elif int(knr) not in kundenr:
                    print("Ikke gyldig kundenummer. Prøv igjen eller skriv EXIT for å avslutte ")
                else:
                    forekomster, StartStasjon, SluttStasjon = OppgaveD()
                    
                    StasjonsTabell = []

                    for ID in forekomster:
                        cursor.execute("""  SELECT DISTINCT ForekomstID, StasjonsNavn, AnkomstTid, AvgangsTid, Dato
                                            FROM RuteTabell_Instans INNER JOIN (Togruteforekomst INNER JOIN Togrute ON Togruteforekomst.TogruteID = Togrute.TogruteID) AS TF ON RuteTabell_Instans.TogruteID = TF.TogruteID
                                            WHERE Togruteforekomst.ForekomstID =:ID 
                                            AND (RuteTabell_Instans.StasjonsNavn =:StartStasjon 
                                            OR RuteTabell_Instans.StasjonsNavn =:SluttStasjon)""", {"ID":ID, "StartStasjon":StartStasjon, "SluttStasjon":SluttStasjon})
                        Mres = cursor.fetchall()
                        StasjonsTabell.append(Mres)


                    LedigeForekomster = []
                    for forekomster in StasjonsTabell:
                        forekomst = forekomster[0][0]
                        LedigeSeter, LedigeKuper = LedigeseterOgSenger(forekomst, StartStasjon, SluttStasjon)

                        ledigeVogner = set(sete[2] for sete in LedigeSeter)
                        ledigeSengeVogner = set(kupe[2] for kupe in LedigeKuper)

                        if not (len(ledigeVogner) == 0 and len(ledigeSengeVogner) == 0):
                            LedigeForekomster.append(forekomster)

                    StasjonsTabell = LedigeForekomster

                    if len(StasjonsTabell) == 0:
                        print("Beklager, ingen forekomster. Prøv annen rute eller dato ")
                        break

                    for f in range(len(StasjonsTabell)):
                        print("Forekomst ", f+1, ": \n"+"-"*50)
                        print("ForekomstID  Stasjon  AnkomstTid  Avgangstid  Dato")
                        for i in range(len(StasjonsTabell[f])-1, -1, -1):
                            if(i == 0):
                                print(StasjonsTabell[f][i], "\n")
                            else:
                                print(StasjonsTabell[f][i])


                    while True:
                        forekomst = input("Hvilken togforekomst ønsker du? ")
                        if (forekomst.isdigit() == False) or (int(forekomst) < 1) or (int(forekomst) >= len(StasjonsTabell)):
                            print("Ikke gyldig forekomst. Prøv igjen \n")
                        else:
                            break
                        
                    while True:
                        LedigeSeter, LedigeKuper = LedigeseterOgSenger(forekomst, StartStasjon, SluttStasjon)
                        print(f"\n Det er {len(LedigeSeter)} sitteplasser og {len(LedigeKuper)} sengeplasser tilgjengelig")
                        antallBilletter = input("Hvor mange billetter ønsker du å kjøpe? ")
                        if (antallBilletter.isdigit() == False) or (int(antallBilletter) < 1):
                            print("Ikke gyldig antall. Prøv igjen \n")
                        else:
                            if ((len(LedigeSeter) + len(LedigeKuper)) < int(antallBilletter)):
                                print(f"Det er kun {len(LedigeSeter) + len(LedigeKuper)} plasser igjen; {len(LedigeSeter)} sitteplasser og {len(LedigeKuper)}. Velg et annet antall ")
                            else:
                                antallBilletter = int(antallBilletter)
                                break
                            
                            
                    CurrentTid = datetime.datetime.now()
                    formatertTid = CurrentTid.strftime("%H:%M %d.%m.%Y")
                    dato = formatertTid.split(" ")[1]
                    tid = formatertTid.split(" ")[0]


                    antallBilletterKjøpt = 0

                    for i in range(antallBilletter):
                    
                        ledigeVogner = set(sete[2] for sete in LedigeSeter)
                        ledigeSengeVogner = set(seng[2] for seng in LedigeKuper)

                        if len(ledigeVogner) == 0 or len(ledigeSengeVogner) == 0:
                            if len(ledigeVogner) == 0:
                                print(f"\n I forekomst {forekomst} er det kun ledige senger")
                                billettType = "seng"
                            else:
                                print(f"\n I forekomst {forekomst} er det kun ledige sitteplasser")
                                billettType = "sete"
                        else:
                            billettType = input("Vil du ha sitteplass eller seng? (SETE/SENG) ").lower()


                        if billettType == "sete":
                            whileCounter = 0
                            while True:
                                whileCounter = 1
                                ledigeVogner = set(sete[2] for sete in LedigeSeter)
                                print("\n Vogner med ledige seter:")
                                for vogn in ledigeVogner:
                                    print(vogn)
                                valgtVogn = input("\n Hvilken vogn velger du? ")
                                if (valgtVogn.isdigit() == False) or (int(valgtVogn) not in ledigeVogner):
                                    print("Ikke gyldig vogn. Prøv igjen \n")
                                else:
                                    while True:
                                        whileCounter = 2
                                        print(f"\n Her er de ledige setene i vogn {valgtVogn}: \n")
                                        seter = []
                                        for sete in LedigeSeter:
                                            if sete[2] == int(valgtVogn):
                                                print(f"Sete {sete[0]} på rad {sete[1]}")
                                                seter.append(sete[0])
                                        valgtSete = input("\n Hvilket sete velger du? ")
                                        if (valgtSete.isdigit() == False) or (int(valgtSete) not in seter):
                                            print("Ikke gyldig sete. Prøv igjen \n")
                                        else:
                                            print(f"\n Du har nå kjøpt billett til sete {valgtSete} i vogn {valgtVogn} \n Forekomst: {forekomst} | Avgang: {StartStasjon} ({StasjonsTabell[int(forekomst)-1][1][3]}) | Ankomst: {SluttStasjon} ({StasjonsTabell[int(forekomst)-1][0][2]})")
                                            antallBilletterKjøpt += 1

                                            if antallBilletterKjøpt == 1:
                                                cursor.execute("""INSERT INTO Kundeordre (Dato, Tid, Antall, Kundenummer) VALUES
                                                                (?, ?, ?, ?)""", (dato, tid, antallBilletter, knr))


                                            cursor.execute("""  SELECT DISTINCT SittevognTilVognoppsett.SittevognID
                                                                FROM SittevognTilVognoppsett INNER JOIN (Vognoppsett INNER JOIN 
                                                                (Togruteforekomst INNER JOIN Togrute ON Togruteforekomst.TogruteID = Togrute.TogruteID) AS FR ON Vognoppsett.OppsettID = FR.OppsettID) 
                                                                AS FRO ON SittevognTilVognoppsett.OppsettID = FRO.OppsettID
                                                                WHERE Togruteforekomst.ForekomstID =:forekomst AND SittevognTilVognoppsett.Vognnummer =:valgvogn""", {"forekomst":forekomst, "valgvogn":valgtVogn})
                                            SittevognID = cursor.fetchall()


                                            cursor.execute("""  SELECT DISTINCT Ordrenummer FROM Kundeordre
                                                                WHERE Kundeordre.Kundenummer =:NR AND Kundeordre.Dato =:dato AND Kundeordre.Tid =:tid""", 
                                                                {"NR":knr, "dato":dato, "tid":tid})
                                            Ordrenummer = cursor.fetchall()


                                            cursor.execute("""  INSERT INTO SeteBillett (Ordrenummer, ForekomstID, Dato, Setenummer, SittevognID) VALUES
                                                                (?, ?, ?, ?, ?)""", (int(Ordrenummer[0][0]), int(forekomst), StasjonsTabell[int(forekomst)-1][0][4], int(valgtSete), int(SittevognID[0][0])))


                                            for sIndeks, sete in enumerate(LedigeSeter):
                                                if ((int(valgtSete) == LedigeSeter[sIndeks][0]) and (int(valgtVogn) == LedigeSeter[sIndeks][2])):
                                                    LedigeSeter.pop(sIndeks)

                                            break
                                        
                                    if whileCounter == 2:
                                        break
                                    
                                    
                        elif billettType == "seng":
                            whileCounter = 0
                            while True:
                                whileCounter = 1
                                ledigeVogner = set(kupe[2] for kupe in LedigeKuper)
                                print("\n Vogner med ledige senger:")
                                for vogn in ledigeVogner:
                                    print(vogn)
                                valgtVogn = input("\n Hvilken vogn velger du? ")
                                if (valgtVogn.isdigit() == False) or (int(valgtVogn) not in ledigeVogner):
                                    print("Ikke gyldig vogn. Prøv igjen \n")
                                else:
                                    while True:
                                        whileCounter = 2
                                        print(f"\n Her er de ledige sengene i vogn {valgtVogn}: \n")
                                        senger = []
                                        for seng in LedigeKuper:
                                            if seng[2] == int(valgtVogn):
                                                print(f"Seng {seng[0]} i kupe {seng[1]}")
                                                senger.append(seng[0])
                                        valgtSeng = input("\n Hvilken seng velger du? ")
                                        if (valgtSeng.isdigit() == False) or (int(valgtSeng) not in senger):
                                            print("Ikke gyldig seng. Prøv igjen \n")
                                        else:
                                            print(f"\n Du har nå kjøpt billett til seng {valgtSeng} i vogn {valgtVogn} \n Forekomst: {forekomst} | Avgang: {StartStasjon} ({StasjonsTabell[int(forekomst)-1][1][3]}) | Ankomst: {SluttStasjon} ({StasjonsTabell[int(forekomst)-1][0][2]})")
                                            antallBilletterKjøpt += 1

                                            if antallBilletterKjøpt == 1:
                                                cursor.execute("""INSERT INTO Kundeordre (Dato, Tid, Antall, Kundenummer) VALUES
                                                                (?, ?, ?, ?)""", (dato, tid, antallBilletter, knr))


                                            for indeks1, seng in enumerate(LedigeKuper):
                                                if ((valgtSeng == str(LedigeKuper[indeks1][0])) and (valgtVogn == str(LedigeKuper[indeks1][2]))):
                                                    LedigeKuper.pop(indeks1)


                                            cursor.execute("""  SELECT DISTINCT SovevognTilVognoppsett.SovevognID
                                                                FROM SovevognTilVognoppsett INNER JOIN (Vognoppsett INNER JOIN 
                                                                (Togruteforekomst INNER JOIN Togrute ON Togruteforekomst.TogruteID = Togrute.TogruteID) AS FR ON Vognoppsett.OppsettID = FR.OppsettID) 
                                                                AS FRO ON SovevognTilVognoppsett.OppsettID = FRO.OppsettID
                                                                WHERE Togruteforekomst.ForekomstID =:forekomst AND SovevognTilVognoppsett.Vognnummer =:valgvogn""", {"forekomst":forekomst, "valgvogn":valgtVogn})
                                            SovevognID = cursor.fetchall()


                                            cursor.execute("""  SELECT DISTINCT Ordrenummer FROM Kundeordre
                                                                WHERE Kundeordre.Kundenummer =:NR AND Kundeordre.Dato =:dato AND Kundeordre.Tid =:tid""", 
                                                                {"NR":knr, "dato":dato, "tid":tid})
                                            Ordrenummer = cursor.fetchall()


                                            cursor.execute("""  INSERT INTO SengBillett (Ordrenummer, ForekomstID, Dato, Sengnummer, SovevognID) VALUES
                                                                (?, ?, ?, ?, ?)""", (int(Ordrenummer[0][0]), int(forekomst), StasjonsTabell[int(forekomst)-1][0][4], int(valgtSeng), int(SovevognID[0][0])))
                                            break 

                                    if whileCounter == 2:
                                        break
                    break
        else:
            print("Ikke gyldig svar. Prøv igjen ")
        if whileCounter == 2:
            break



def LedigeseterOgSenger(forekomst, StartStasjon, SluttStasjon):
    
    #SETER
    
    cursor.execute("""  SELECT SittevognID, VognNummer   
                            FROM (SittevognTilVognoppsett INNER JOIN (Togruteforekomst INNER JOIN Togrute ON Togruteforekomst.TogruteID = Togrute.TogruteID) AS Forekomst 
                            ON SittevognTilVognoppsett.OppsettID = Forekomst.OppsettID)
                            WHERE Togruteforekomst.ForekomstID =:forekomst """, {"forekomst":forekomst})
    Sittevognoppsett = cursor.fetchall()


    SeteplassListe = []
    for vogner in Sittevognoppsett:
        cursor.execute("""  SELECT DISTINCT Setenummer, Radnummer, Vognnummer, Sittevogn.SittevognID
                            FROM SittevognTilVognoppsett INNER JOIN (Sittevogn INNER JOIN Sitteplass ON Sittevogn.SittevognID = Sitteplass.SittevognID) ON SittevognTilVognoppsett.SittevognID = Sittevogn.SittevognID
                            WHERE Sittevogn.SittevognID =:ID""", {"ID":vogner[0]})
        SeteplassListe.append(cursor.fetchall())


    cursor.execute("""  SELECT DISTINCT SeteBillett.BillettID, OrdreNummer, ForekomstID, TogruteID, StasjonsNavn, SeteBillett.Setenummer, SittevognTilVognoppsett.Vognnummer
                        FROM SittevognTilVognoppsett INNER JOIN (SitteVogn INNER JOIN 
                        (SeteBillett INNER JOIN SeteBillett_StartEllerSlutt ON SeteBillett.BillettID = SeteBillett_StartEllerSlutt.BillettID) AS Billett 
                        ON SitteVogn.SittevognID = Billett.SittevognID) AS SV ON SittevognTilVognoppsett.SittevognID = SV.SittevognID
                        WHERE SeteBillett.ForekomstID =:ID""", {"ID": forekomst})
    EksisterendeBilletter = cursor.fetchall()


    cursor.execute("""  SELECT DISTINCT StasjonsNavn
                        FROM RuteTabell_Instans INNER JOIN (Togruteforekomst INNER JOIN Togrute ON Togruteforekomst.TogruteID = Togrute.TogruteID) AS TF ON RuteTabell_Instans.TogruteID = TF.TogruteID
                        WHERE Togruteforekomst.ForekomstID =:ID""", {"ID": forekomst})
    ForekomstStasjoner = cursor.fetchall()


    KundeStasjoner = []
    Behold = False
    for tup in ForekomstStasjoner:
        if tup[0] == SluttStasjon:
            Behold = not Behold
        elif tup[0] == StartStasjon:
            KundeStasjoner.append(tup[0])
            Behold = not Behold
        if Behold:
            KundeStasjoner.append(tup[0])


    OpptatteSitteplasser = []
    Opptatt = False
    for i in range(len(EksisterendeBilletter)):
        BillettStartSlutt = []
        if i%2 == 0:
            BillettStartSlutt.append(EksisterendeBilletter[i][0])
            BillettStartSlutt.append(EksisterendeBilletter[i][4])
            BillettStartSlutt.append(EksisterendeBilletter[i+1][4])
        else:
            continue

        BillettStasjoner = []
        Behold = False

        for tup in ForekomstStasjoner:
            if tup[0] == BillettStartSlutt[2]:
                Behold = not Behold
            elif tup[0] == BillettStartSlutt[1]:
                BillettStasjoner.append(tup[0])
                Behold = not Behold
            if Behold:
                BillettStasjoner.append(tup[0])
        counter = 0

        for KundeStasjon in KundeStasjoner:
            if KundeStasjon in BillettStasjoner:
                counter += 1
            if counter >= 2:
                Opptatt = True

        if Opptatt == True:
            liste = []
            liste.append(EksisterendeBilletter[i][5])
            liste.append(EksisterendeBilletter[i][6])
            OpptatteSitteplasser.append(liste)


    LedigeSeter = []
    for vIndeks, vogn in enumerate(SeteplassListe):
        for sIndeks, sete in enumerate(SeteplassListe[vIndeks]):
            SeteOgVogn = list(sete)
            SeteOgVogn.pop(3)
            SeteOgVogn.pop(1)
            if SeteOgVogn not in OpptatteSitteplasser:
                LedigeSeter.append(SeteplassListe[vIndeks][sIndeks])

    #SENGER 

    SengePlassListe = []
    cursor.execute("""  SELECT SovevognID, VognNummer    
                        FROM (SovevognTilVognoppsett INNER JOIN 
                        (Togruteforekomst INNER JOIN Togrute ON Togruteforekomst.TogruteID = Togrute.TogruteID) AS ForekomstOppsett 
                        ON SovevognTilVognoppsett.OppsettID = ForekomstOppsett.OppsettID)
                        WHERE Togruteforekomst.ForekomstID =:forekomst""", {"forekomst":forekomst})
    Sovevognoppsett = cursor.fetchall()


    for vogner in Sovevognoppsett:
        cursor.execute("""  SELECT DISTINCT Sengnummer, Kupenummer, Vognnummer, Sovevogn.SovevognID
                            FROM SovevognTilVognoppsett INNER JOIN (Sovevogn INNER JOIN Seng ON Sovevogn.SovevognID = Seng.SovevognID) ON SovevognTilVognoppsett.SovevognID = Sovevogn.SovevognID
                            WHERE Sovevogn.SovevognID =:ID""", {"ID":vogner[0]})
        SengePlassListe.append(cursor.fetchall())

        
    cursor.execute("""  SELECT DISTINCT Sovevogn.SovevognID, Ordrenummer, ForekomstID, TogruteID, StasjonsNavn, SengBillett.Sengnummer, Seng.Kupenummer, SovevognTilVognoppsett.Vognnummer
                        FROM Seng INNER JOIN (SovevognTilVognoppsett INNER JOIN( Sovevogn INNER JOIN (SengBillett INNER JOIN SengBillett_StartEllerSlutt ON SengBillett.BillettID = SengBillett_StartEllerSlutt.BillettID) AS Billett
                        ON Sovevogn.SovevognID = Billett.SovevognID) AS SV ON SovevognTilVognoppsett.SovevognID = SV.SovevognID) AS ESB ON Seng.Sengnummer = ESB.Sengnummer
                        WHERE SengBillett.ForekomstID =:ID AND Seng.SovevognID = ESB.SovevognID""", {"ID": forekomst})
    EksisterendeSengeBilletter = cursor.fetchall()
    
    
    OpptatteKupeplasser = []
    for Billett in EksisterendeSengeBilletter:
        for stasjoner in ForekomstStasjoner:
            if Billett[4] in stasjoner[0]:
                Mlist = []
                Mlist.append(Billett[6])
                Mlist.append(Billett[7])
                if not Mlist in OpptatteKupeplasser:
                        OpptatteKupeplasser.append(Mlist)
    Ledigekuper = []
    for vIndeks, vogn in enumerate(SengePlassListe):
        for sIndeks, seng in enumerate(SengePlassListe[vIndeks]):
            KupeOgVogn = list(seng)
            KupeOgVogn.pop(3)
            KupeOgVogn.pop(0)
            if KupeOgVogn not in OpptatteKupeplasser:
                Ledigekuper.append(SengePlassListe[vIndeks][sIndeks])

    return LedigeSeter, Ledigekuper



#Oppgave h)

def OppgaveH():    
    
    bruker = input("For hvilken bruker vil du hente ut kjøpsinformasjon? ")    

    cursor.execute("""  SELECT Kunde.Navn, Kundeordre.Ordrenummer, Kundeordre.Antall, Kundeordre.Kundenummer, Kundeordre.Dato, Kundeordre.Tid, SeteBillett.BillettID, SeteBillett.ForekomstID, SeteBillett.Dato, SeteBillett.Setenummer, SeteBillett.SittevognID
                        FROM SeteBillett INNER JOIN (Kunde INNER JOIN Kundeordre ON Kunde.Kundenummer = Kundeordre.Kundenummer) AS KU ON SeteBillett.Ordrenummer = KU.Ordrenummer
                        WHERE Kunde.Kundenummer =:kundenr
                        ORDER BY Kundeordre.Ordrenummer ASC""", {"kundenr":bruker})

    SeteBrukerInfo = cursor.fetchall()

    cursor.execute("""  SELECT Kunde.Navn, Kundeordre.Ordrenummer, Kundeordre.Antall, Kundeordre.Kundenummer, Kundeordre.Dato, Kundeordre.Tid, SengBillett.BillettID, SengBillett.ForekomstID, SengBillett.Dato, SengBillett.Sengnummer, SengBillett.SovevognID
                        FROM SengBillett INNER JOIN (Kunde INNER JOIN Kundeordre ON Kunde.Kundenummer = Kundeordre.Kundenummer) AS KU ON SengBillett.Ordrenummer = KU.Ordrenummer
                        WHERE Kunde.Kundenummer =:kundenr""", {"kundenr":bruker})
    
    SengBrukerInfo = cursor.fetchall()
    

    dateNå = datetime.datetime.now()
    formatert = dateNå.strftime("%H:%M %d.%m.%Y")
    datoNå = formatert.split(" ")[1]

    FremtidigInfo = []
    FremtidigSeteInfo = []
    FremtidigSengInfo = []

    for info in SeteBrukerInfo:
        if datetime.date(int(info[8].split(".")[2]), int(info[8].split(".")[1]), int(info[8].split(".")[0])) > datetime.date(int(datoNå.split(".")[2]), int(datoNå.split(".")[1]), int(datoNå.split(".")[0])):
            FremtidigSeteInfo.append(info)

    for info in SengBrukerInfo:
        if datetime.date(int(info[8].split(".")[2]), int(info[8].split(".")[1]), int(info[8].split(".")[0])) > datetime.date(int(datoNå.split(".")[2]), int(datoNå.split(".")[1]), int(datoNå.split(".")[0])):
            FremtidigSengInfo.append(info)
    
    Ordre = []
    mt = 0
    for i in range(len(FremtidigSeteInfo)):
        if i == 0:
            Ordrenummer = FremtidigSeteInfo[i][1]
            Ordre.append(FremtidigSeteInfo[i])
        else:
            if Ordrenummer == FremtidigSeteInfo[i][1]:
                Ordre.append(FremtidigSeteInfo[i])
            else:
                for j in range(len(FremtidigSengInfo)):
                    if Ordrenummer == FremtidigSengInfo[j][1]:
                        if mt == 0:
                            Ordre.append("Bytte")
                            mt +=1
                        Ordre.append(FremtidigSengInfo[j])
                mt = 0
                FremtidigInfo.append(Ordre)
                Ordre = []
                Ordre.append(FremtidigSeteInfo[i])
                Ordrenummer = FremtidigSeteInfo[i][1]
                if i == len(FremtidigSeteInfo)-1:
                    for j in range(len(FremtidigSengInfo)):
                        if Ordrenummer == FremtidigSengInfo[j][1]:
                            if mt == 0:
                                Ordre.append("Bytte")
                                mt +=1
                        Ordre.append(FremtidigSengInfo[j])
                    FremtidigInfo.append(Ordre)        
    teller = 0
    Sete = 1
    for i in range(len(FremtidigInfo)):
        for j in range(len(FremtidigInfo[i])):
            if teller == 0:
                teller += 1
                print(f"Kundenavn: {FremtidigInfo[i][j][0]} | Kundenummer: {FremtidigInfo[i][j][3]} \n" + "-"*90)   
                print(f"Ordrenummer: {FremtidigInfo[i][j][1]} | OrdreDato: {FremtidigInfo[i][j][4]}| OrdreTid: {FremtidigInfo[i][j][5]}  Antall Billeter: {FremtidigInfo[i][j][2]} \n"+ "-"*90)
            if FremtidigInfo[i][j] == "Bytte":
                Sete = 0
            elif Sete == 1:
                cursor.execute("""  SELECT DISTINCT SeteBillett_StartEllerSlutt.TogruteID, RuteTabell_Instans.StasjonsNavn, RuteTabell_Instans.Ankomsttid, RuteTabell_Instans.AvgangsTid
                                    FROM SeteBillett_StartEllerSlutt INNER JOIN RuteTabell_Instans ON SeteBillett_StartEllerSlutt.StasjonsNavn = RuteTabell_Instans.StasjonsNavn
                                    WHERE SeteBillett_StartEllerSlutt.BillettID =:noe AND RuteTabell_Instans.TogruteID = SeteBillett_StartEllerSlutt.TogruteID""", {"noe":FremtidigInfo[i][j][6]})
                SeteStasjoner = cursor.fetchall()
                print(f"Billett {teller} --> SeteBillettID: {FremtidigInfo[i][j][6]} | ForekomstID: {FremtidigInfo[i][j][7]} | Dato : {FremtidigInfo[i][j][8]} | Setenummer: {FremtidigInfo[i][j][9]} | SetevognID : {FremtidigInfo[i][j][10]} | TogruteID : {SeteStasjoner[0][0]} | StartStasjon : {SeteStasjoner[1][1]} | Avgangstid : {SeteStasjoner[1][3]} | Endestasjon : {SeteStasjoner[0][1]} | Ankomsttid : {SeteStasjoner[0][2]} \n")
                teller += 1
            else:
                cursor.execute("""  SELECT DISTINCT SengBillett_StartEllerSlutt.TogruteID, RuteTabell_Instans.StasjonsNavn, RuteTabell_Instans.Ankomsttid, RuteTabell_Instans.AvgangsTid
                                    FROM SengBillett_StartEllerSlutt INNER JOIN RuteTabell_Instans ON SengBillett_StartEllerSlutt.StasjonsNavn = RuteTabell_Instans.StasjonsNavn
                                    WHERE SengBillett_StartEllerSlutt.BillettID =:noe AND RuteTabell_Instans.TogruteID = SengBillett_StartEllerSlutt.TogruteID""", {"noe":FremtidigInfo[i][j][6]})
                SengStasjoner = cursor.fetchall()
                print(f"Billett {teller} --> SengBillettID: {FremtidigInfo[i][j][6]} | ForekomstID: {FremtidigInfo[i][j][7]} | Dato : {FremtidigInfo[i][j][8]} | Sengnummer: {FremtidigInfo[i][j][9]} | SengvognID : {FremtidigInfo[i][j][10]} | TogruteID : {SengStasjoner[0][0]} | StartStasjon : {SengStasjoner[1][1]} | Avgangstid : {SengStasjoner[1][3]} | Endestasjon : {SengStasjoner[0][1]} | Ankomsttid : {SengStasjoner[0][2]} \n")
                teller += 1
                
            Ordrenummer = FremtidigInfo[i][j][1]



    


def main():
    pre()
    print()
    print("                                    Velkommen til Nordlandsbanen! Hva vil du gjøre i dag?                                     ")
    print("    ----------------------------------------------------------------------------------------------------------------------    ")
    print("    Sjekke togruter fra stasjon:   |   Sjekke forekomster fra én stasjon til en annen:   |   Registrere i kunderegisteret:    ")
    print("              (Trykk C)            |                    (Trykk D)                        |           (Trykk E)                ")
    print("    ----------------------------------------------------------------------------------------------------------------------    ")                 
    print("    Registrere i kunderegisteret:  |                  Kjøpe billett:                     |  Informasjon om tidligere kjøp:    ")
    print("              (Trykk E)            |                    (Trykk G)                        |           (Trykk H)                \n\n")              
    ønske = input("(Forlate programmet: Skriv EXIT)                            ").lower()
    if ønske == "c":
        OppgaveC()
    elif ønske == "d":
        OppgaveD()
    elif ønske == "e":
        OppgaveE()
    elif ønske == "g":
        OppgaveG()
    elif ønske == "h":
        OppgaveH()
    elif ønske == "exit":
        print("Hadebra! ")

    #con.commit()
    con.close()
    return


main()



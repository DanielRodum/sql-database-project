CREATE TABLE Jernbanestasjon (
	Navn TEXT,
	Hoyde REAL,
	PRIMARY KEY (Navn)
);

CREATE TABLE Banestrekning (
	Navn TEXT,
	Fremdriftsenergi TEXT,
	B_Startstasjon TEXT NOT NULL,
	B_Endestasjon TEXT NOT NULL,
	PRIMARY KEY (Navn),
	FOREIGN KEY (B_Startstasjon) REFERENCES Jernbanestasjon (Navn) 
		ON DELETE CASCADE
		ON UPDATE CASCADE, 
	FOREIGN KEY (B_Endestasjon) REFERENCES Jernbanestasjon (Navn)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE B_Mellomstasjon (
	Mellomstasjon_Navn TEXT,
	Banestrekning_Navn TEXT NOT NULL,
	PRIMARY KEY (Mellomstasjon_Navn),
	FOREIGN KEY (Mellomstasjon_Navn) REFERENCES Jernbanestasjon (Navn)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	FOREIGN KEY (Banestrekning_Navn) REFERENCES Banestrekning (Navn)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE Delstrekning (
	DelstrekningID INTEGER PRIMARY KEY,
	Lengde INTEGER,
	Sportype TEXT,
	Banestrekning_Navn TEXT NOT NULL,
	StasjonEn TEXT NOT NULL,
	StasjonTo TEXT NOT NULL,
	FOREIGN KEY (Banestrekning_Navn) REFERENCES Banestrekning (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (StasjonEn) REFERENCES Jernbanestasjon (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
	FOREIGN KEY (StasjonTo) REFERENCES Jernbanestasjon (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Kunderegister (
	RegisterID INTEGER PRIMARY KEY
);

CREATE TABLE Operator (
	Navn TEXT,
	Kunderegister INTEGER NOT NULL,
	PRIMARY KEY (Navn),
	FOREIGN KEY (Kunderegister) REFERENCES Kunderegister (RegisterID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Vognoppsett (
	OppsettID INTEGER PRIMARY KEY
);

CREATE Table Togrute (
	TogruteID INTEGER PRIMARY KEY,
	Operator_Navn TEXT NOT NULL,
	Banestrekning_Navn TEXT NOT NULL,
	Retning TEXT,
	OppsettID INTEGER NOT NULL,
	FOREIGN KEY (Operator_Navn) REFERENCES Operator (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Banestrekning_Navn) REFERENCES Banestrekning (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN key (OppsettID) REFERENCES Vognoppsett (OppsettID)
		ON DELETE CASCADE									
		ON UPDATE NO ACTION
);

CREATE TABLE RuteTabell_Instans (
	TogruteID INTEGER,
	StasjonsNavn TEXT,
	Ukedag TEXT, 
	AnkomstTid TIME,
	AvgangsTid TIME,
	PRIMARY KEY (TogruteID, StasjonsNavn, Ukedag),
	FOREIGN KEY (TogruteID) REFERENCES Togrute (TogruteID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (StasjonsNavn) REFERENCES Jernbanestasjon (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Togruteforekomst (
	ForekomstID INTEGER,
	Dato DATE,
	TogruteID INTEGER NOT NULL,
	PRIMARY KEY (ForekomstID, Dato),
	FOREIGN KEY (TogruteID) REFERENCES Togrute (TogruteID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Kunde (
	Kundenummer INTEGER PRIMARY KEY,
	Navn TEXT,
	Epost TEXT,
	Mobilnummer INTEGER,
	RegisterID INTEGER NOT NULL,
	FOREIGN KEY (RegisterID) REFERENCES Kunderegister (RegisterID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Kundeordre (
	Ordrenummer INTEGER PRIMARY KEY,
	Dato DATE,
	Tid TIME,
	Antall INTEGER,
	Kundenummer INTEGER,
	FOREIGN key (Kundenummer) REFERENCES Kunde (Kundenummer)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Sovevogn (
	SovevognID INTEGER PRIMARY KEY,
	Navn TEXT,
	Operator_Navn TEXT NOT NULL,
	FOREIGN KEY (Operator_Navn) REFERENCES Operator (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Sovekupe (
	Kupenummer INTEGER,
	SovevognID INTEGER, 	
	PRIMARY KEY (Kupenummer, SovevognID),
	FOREIGN KEY (SovevognID) REFERENCES Sovevogn (SovevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Seng (
	Sengnummer INTEGER,
	SovevognID INTEGER,
	Kupenummer INTEGER NOT NULL,
	PRIMARY KEY (Sengnummer, SovevognID),
	FOREIGN KEY (SovevognID) REFERENCES Sovevogn (SovevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Kupenummer) REFERENCES Sovekupe (Kupenummer)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE SengBillett (
	BillettID INTEGER PRIMARY KEY,
	Ordrenummer INTEGER NOT NULL,
	ForekomstID INTEGER NOT NULL,
	Dato DATE NOT NULL,
	Sengnummer INTEGER NOT NULL,
	SovevognID INTEGER NOT NULL,
	FOREIGN KEY (Ordrenummer) REFERENCES Kundeordre (Ordrenummer)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (ForekomstID) REFERENCES Togruteforekomst (ForekomstID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Dato) REFERENCES Togruteforekomst (Dato)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Sengnummer) REFERENCES Seng (Sengnummer)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
	FOREIGN KEY (SovevognID) REFERENCES Seng (SovevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Sittevogn (
	SittevognID INTEGER PRIMARY KEY,
	Navn TEXT,
	Operator_Navn TEXT NOT NULL,
	FOREIGN KEY (Operator_Navn) REFERENCES Operator (Navn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Rad (
	Radnummer INTEGER,
	SittevognID INTEGER,
	PRIMARY KEY (Radnummer, SittevognID),
	FOREIGN KEY (SittevognID) REFERENCES Sittevogn (SittevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE Sitteplass (
	Setenummer INTEGER,
	SittevognID INTEGER,
	Radnummer INTEGER NOT NULL,
	PRIMARY KEY (Setenummer, SittevognID),
	FOREIGN KEY (SittevognID) REFERENCES Sittevogn (SittevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Radnummer) REFERENCES Rad (Radnummer)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE SeteBillett (
	BillettID INTEGER PRIMARY KEY,
	Ordrenummer INTEGER NOT NULL,
	ForekomstID INTEGER NOT NULL,
	Dato DATE NOT NULL,
	Setenummer INTEGER NOT NULL,
	SittevognID INTEGER NOT NULL,
	FOREIGN KEY (Ordrenummer) REFERENCES Kundeordre (Ordrenummer)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (ForekomstID) REFERENCES Togruteforekomst (ForekomstID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Dato) REFERENCES Togruteforekomst (Dato)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Setenummer) REFERENCES Sitteplass (Setenummer)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
	FOREIGN KEY (SittevognID) REFERENCES Sitteplass (SittevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE SengBillett_StartEllerSlutt (
	BillettID INTEGER,
	TogruteID INTEGER,
	StasjonsNavn TEXT,
	Ukedag TEXT,
	PRIMARY KEY (BillettID, TogruteID, StasjonsNavn, Ukedag),
	FOREIGN KEY (BillettID) REFERENCES SengBillett (BillettID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (TogruteID) REFERENCES RuteTabell_Instans (TogruteID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (StasjonsNavn) REFERENCES RuteTabell_Instans (StasjonsNavn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Ukedag) REFERENCES RuteTabell_Instans (Ukedag)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE SeteBillett_StartEllerSlutt (
	BillettID INTEGER,
	TogruteID INTEGER,
	StasjonsNavn TEXT,
	Ukedag TEXT,
	PRIMARY KEY (BillettID, TogruteID, StasjonsNavn, Ukedag),
	FOREIGN KEY (BillettID) REFERENCES SeteBillett (BillettID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (TogruteID) REFERENCES RuteTabell_Instans (TogruteID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (StasjonsNavn) REFERENCES RuteTabell_Instans (StasjonsNavn)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (Ukedag) REFERENCES RuteTabell_Instans (Ukedag)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE SovevognTilVognoppsett (
	SovevognID INTEGER,
	OppsettID INTEGER,
	Vognnummer INTEGER,
	PRIMARY KEY (SovevognID, OppsettID),
	FOREIGN KEY (SovevognID) REFERENCES Sovevogn (SovevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (OppsettID) REFERENCES Vognoppsett (OppsettID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);

CREATE TABLE SittevognTilVognoppsett (
	SittevognID INTEGER,
	OppsettID INTEGER,
	Vognnummer INTEGER,
	PRIMARY KEY (SittevognID, OppsettID),
	FOREIGN KEY (SittevognID) REFERENCES Sittevogn (SittevognID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	FOREIGN KEY (OppsettID) REFERENCES Vognoppsett (OppsettID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION
);
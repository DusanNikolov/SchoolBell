/////////////////////////////////////////////////
///                                           ///
///                  README                   ///
///                                           ///
/////////////////////////////////////////////////

<<< CONFIGURATION >>>

<< WINAMP SETTINGS >>
1. Skinuti Winamp sa adrese: http://winamp.meggamusic.co.uk/winamp5666_full_en-us_redux.exe

2. Instalirati Winamp u podrazumevani direktorijum: C:\Program Files\Winamp,
   ili ako se menja direktorijum, pratiti uputstvo u delu za modifikovanje konfiguracionih fajlova

3. Podesiti skin u Winamp-u na classic: Desni klik na Winamp toolbar->Skins->Winamp Classic


<< PYTHON SETTINGS >>
1. Skinuti Python 2.7 sa adrese: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

2. Instalirati Python u podrazumevani direktorijum: C:\Python27

3. Proveriti da li je putanja do python.exe dodata u "Path" Environment Variable i ako nije dodati

    3.1 Otvoriti Control Panel -> System -> Advanced System Settings -> Environment Variables...
    3.2 U delu System Variables pronaci Path promenljivu i dodati putanju "C:\Python27;" (bez navodnika)
        na pocetak, ukoliko vec ne postoji

4. Skinuti pywin32 plugin za Python i instalirati ga sa adrese:
   http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download


<< WINDOWS TASK SCHEDULER >>
1. Neophodno je formirati nov task koji ce izvrsavati Python skriptu
2. Otvoriti Task Scheduler
    2.1 Action -> Create Task...
    2.2 Podesavanje novog taska:
        General     - Name: SchoolBell
        Triggers    - New...
            Begin the task: On the schedule
            Settings:
                Start time: 00:00:00
                Weekly
                Recur every 1 weeks on: Monday, Tuesday, Wednesday, Thursday, Friday
            Advanced settings:
                Repeat task every: 1 minutes for a duration of: Indefinitely
                Enabled
        Actions     - New...
            Action: Start a program
            Settings:
                Program/script: C:\Python27\python.exe (promeniti putanju ukoliko je Python instaliran na drugoj lokaciji)
                Add arguments: SchoolBell.py
                Start in: C:\SchoolBell (promeniti putanju ukoliko je program smesten na drugu lokaciju)
3. Ovim je task podesen da na svakih 1 minuta pokrece skriptu koja kontrolise rad zvona i pustanje muzike


<< CONFIGURATION FILES >>
1. Dozvoljeno je menjati samo konfiguracioni fajl "main_configuration.ini"!

    winamp_path - ukoliko se Winamp ne instalira u podrazumevani direktorijum, neophodno je izmeniti vrednost
                ove promenljive tako da sadrzi putanju direktorijuma u kome se nalazi winamp.exe fajl

    select_schedule - vrednost ove promenljive se menja u skladu sa tekucim vazecim rasporedom casova:
        REGULAR - redovan raspored casova i zvonjenja
        SHORT   - raspored casova i zvonjenja za vreme skolskih priredbi i predstava
        STRIKE  - raspored casova i zvonjenja za vreme strajka

2. Ukoliko je neophodno, moguce je izmeniti i konfiguracione fajlove koji sadrze rasporede zvonjenja.
   Fajlovi se nalaze u direktorijumu "configurations" i format fajlova je precizan i neophodno ga je postovati
   da bi se obezbedio ispravan rad programa:

        Svi fajlovi sadrze dve sekcije sa rasporedom zvonjenja - [FIRST_SHIFT] i [SECOND_SHIFT];
        Unutar sekcija vremena su oznacena u 24H formatu kao:

            START_BREAK_?   - vrednost je vreme u formatu "HH:MM" i predstavlja pocetak odmora ( kraj prethodnog casa)
            STOP_BREAK_?    - vrednost je vreme u formatu "HH:MM" i predstavlja kraj odmora (pocetak narednog casa)


<< PLAYLIST FILE >>
1. Neophodno je formirati playlist.m3u fajl sa muzikom koja ce biti pustana za vreme odmora.
2. Ucitati svu muziku u Winamp i sacuvati je u direktorijum "sounds" pod imenom playlist.m3u



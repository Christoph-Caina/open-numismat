[Setup]
AppName=OpenNumismat
AppId=OpenNumismat
AppVersion=1.5.2
DefaultDirName={pf}\OpenNumismat
DefaultGroupName=OpenNumismat
UninstallDisplayIcon={app}\OpenNumismat.exe
OutputDir="."
OutputBaseFilename="OpenNumismat-1.5.2"
AllowNoIcons=yes
AppCopyright=Copyright 2011-2015 by Vitaly Ignatov
AppPublisher=Janis

[Languages]
Name: en; MessagesFile: "compiler:Default.isl"; InfoBeforeFile: license_en.txt
Name: ru; MessagesFile: "compiler:Languages\Russian.isl"; InfoBeforeFile: license_ru.txt
Name: uk; MessagesFile: "compiler:Languages\Ukrainian.isl"; InfoBeforeFile: license_uk.txt
Name: es; MessagesFile: "compiler:Languages\Spanish.isl"; InfoBeforeFile: license_es.txt
Name: fr; MessagesFile: "compiler:Languages\French.isl"; InfoBeforeFile: license_fr.txt
Name: hu; MessagesFile: "compiler:Languages\Hungarian.isl"; InfoBeforeFile: license_en.txt
Name: pt; MessagesFile: "compiler:Languages\Portuguese.isl"; InfoBeforeFile: license_pt.txt
Name: de; MessagesFile: "compiler:Languages\German.isl"; InfoBeforeFile: license_de.txt
Name: el; MessagesFile: "compiler:Languages\Greek.isl"; InfoBeforeFile: license_en.txt
Name: cs; MessagesFile: "compiler:Languages\Czech.isl"; InfoBeforeFile: license_en.txt
Name: it; MessagesFile: "compiler:Languages\Italian.isl"; InfoBeforeFile: license_it.txt
Name: pl; MessagesFile: "compiler:Languages\Polish.isl"; InfoBeforeFile: license_pl.txt

[CustomMessages]
en.sendReport=Send a reports to author's web-site if any error occurred
ru.sendReport=�������� ����� ������������ ��� ������������� ������
uk.sendReport=³��������� ��� ������ ��� ��������� �������
es.sendReport=Enviar un informe al autor del sitio web si cualquier error
fr.sendReport=Envoyer un rapport a l'auteur du site-web si une erreur se produit.
hu.sendReport=Hiba elkuldese a keszitonek
pt.sendReport=Enviar um relatorio para o site do autor se ocorrer um erro
de.sendReport=Send a reports to author's web-site if any error occurred
el.sendReport=Send a reports to author's web-site if any error occurred
cs.sendReport=Send a reports to author's web-site if any error occurred
it.sendReport=Invia un rapporto al sito web dell'autore se e avvenuto un errore
pl.sendReport=Wyslij raport do Autorow w przypadku problemow

en.checkUpdate=Automatically check for updates
ru.checkUpdate=��������� ���������� �������������
uk.checkUpdate=��������� ��������� �����������
es.checkUpdate=Automatically check for updates
fr.checkUpdate=Verification automatique des mises a jour
hu.checkUpdate=Automatically check for updates
pt.checkUpdate=Procurar atualizacoes automaticamente
de.checkUpdate=Automatically check for updates
el.checkUpdate=Automatically check for updates
cs.checkUpdate=Automatically check for updates
it.checkUpdate=Cerca automaticamente gli aggiornamenti
pl.checkUpdate=Automatycznie sprawdzaj w poszukiwaniu najnowszej wersji

en.associate=Associate *.db files with OpenNumismat
ru.associate=������� *.db ����� � OpenNumismat
uk.associate=����������� ����� *.db � OpenNumismat
es.associate=Associate *.db files with OpenNumismat
fr.associate=Associer les fichiers *.db avec OpenNumismat
hu.associate=Associate *.db files with OpenNumismat
pt.associate=Associar ficheiros *.db com o OpenNumismat
de.associate=Associate *.db files with OpenNumismat
el.associate=Associate *.db files with OpenNumismat
cs.associate=Associate *.db files with OpenNumismat
it.associate=Associare i file *.db con OpenNumismat
pl.associate=Skojarz rozszerzenie *.db z OpenNumismat

[Files]
Source: "..\build\exe.win32-3.4\*"; DestDir: "{app}"; Flags: recursesubdirs ignoreversion
Source: "..\build\exe.win32-3.4\db\demo_en.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: en; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_ru.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: ru; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_uk.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: uk; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_es.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: es; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_fr.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: fr; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_hu.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: hu; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_pt.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: pt; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_de.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: de; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_el.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: el; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_cs.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: cs; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_it.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: it; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\demo_pl.db"; DestDir: "{userdocs}\OpenNumismat"; DestName: "demo.db"; Languages: pl; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_en.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: en; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_ru.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: ru; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_uk.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: uk; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_es.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: es; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_fr.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: fr; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_hu.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: hu; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_pt.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: pt; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_de.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: de; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_el.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: el; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_cs.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: cs; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_it.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: it; Flags: onlyifdoesntexist
Source: "..\build\exe.win32-3.4\db\reference_pl.ref"; DestDir: "{userdocs}\OpenNumismat"; DestName: "reference.ref"; Languages: pl; Flags: onlyifdoesntexist

[Dirs]
Name: "{userdocs}\OpenNumismat\backup"

[Registry]
Root: HKCU; Subkey: "Software\Janis"; Flags: uninsdeletekeyifempty
Root: HKCU; Subkey: "Software\Janis\OpenNumismat"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Janis\OpenNumismat\mainwindow"; ValueType: string; ValueName: "error"; ValueData: "true"; Tasks: sendreport
Root: HKCU; Subkey: "Software\Janis\OpenNumismat\mainwindow"; ValueType: string; ValueName: "updates"; ValueData: "true"; Tasks: checkupdate
Root: HKCR; Subkey: ".db"; ValueType: string; ValueName: ""; ValueData: "OpenNumismatCollection"; Flags: uninsdeletevalue; Tasks: associate 
Root: HKCR; Subkey: "OpenNumismatCollection"; ValueType: string; ValueName: ""; ValueData: "OpenNumismat collection"; Flags: uninsdeletekey; Tasks: associate
Root: HKCR; Subkey: "OpenNumismatCollection\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\OpenNumismat.EXE,0"; Flags: uninsdeletekey; Tasks: associate
Root: HKCR; Subkey: "OpenNumismatCollection\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\OpenNumismat.EXE"" ""%1"""; Flags: uninsdeletekey; Tasks: associate

[Icons]
Name: "{group}\OpenNumismat"; Filename: "{app}\OpenNumismat.exe"
Name: "{group}\Uninstall OpenNumismat"; Filename: "{uninstallexe}"
Name: "{userdesktop}\OpenNumismat"; Filename: "{app}\OpenNumismat.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\OpenNumismat"; Filename: "{app}\OpenNumismat.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\OpenNumismat.exe"; Flags: postinstall nowait skipifsilent

[Tasks]
Name: associate; Description: "{cm:associate}"; Flags: unchecked
Name: sendreport; Description: "{cm:sendReport}"
Name: checkupdate; Description: "{cm:checkUpdate}"
Name: desktopicon; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
Name: quicklaunchicon; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

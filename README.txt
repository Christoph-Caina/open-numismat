Requirement:
 * Python 3.4.4
 * PyQt5 5.5.1
 * Jinja2 2.10 (for reports)
 * Matplotlib 2.1.0 (for statistics)
 * xlwt-future 0.8.0 (for exporting to Excel)
 * pywin32-219 (for saving report as Word Document)
 * lxml 3.4.1 (for importing from CoinsCollector 2.6 and Tellico)
 * xlrd 1.1.0 (for importing from Excel)
 * python-dateutil 2.6.1 (for importing from Excel)
 * Firebird 2.0 (for importing from Numizmat 2.1)
 * pyfirebirdsql 0.9.12 (for importing from Numizmat 2.1)
 * pyodbc 3.0.10 (for importing from Cabinet 2.0.2.0, 2011 and CoinManage 2011)
 * DBISAM ODBC-TRIAL 4.3 (for importing from Cabinet 2.0.2.0, 2011)
 * Visual FoxPro ODBC Driver, Microsoft Access Database Engine, Microsoft Access or any other
   software with ODBC {Microsoft Access Driver (*.mdb)} (for importing from CoinManage 2011)
 * cx_Freeze 4.3.4 (for deploy)
 * Inno Setup 5.5.9 (for deploy)
 * Delphi Delphi XE2 (for building CdrToXml.dll for importing from CoinsCollector 2.6)

Deploying:
Run `python setup.py build_exe`
Compile setup*.iss with Inno Setup

import wx
import wx.grid
import mysql.connector
import history


mydb2 = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_simak"
)


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(750, 560), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer4.SetMinSize(wx.Size(1200, 800))
        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 800), 0)
        self.m_panel6 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self.m_panel6, wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size(100, -1), 0)
        self.m_staticText7.Wrap(-1)
        bSizer16.Add(self.m_staticText7, 0, wx.ALL, 5)

        m_choice7Choices = [u"2018", u"2017"]
        self.m_choice7 = wx.Choice(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), m_choice7Choices, 0)
        self.m_choice7.SetSelection(0)
        self.m_choice7.SetMinSize(wx.Size(100, -1))

        bSizer16.Add(self.m_choice7, 0, wx.ALL, 5)

        bSizer13.Add(bSizer16, 1, wx.EXPAND, 5)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)


        self.m_grid6 = wx.grid.Grid(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid6.CreateGrid(10, 5)
        self.m_grid6.EnableEditing(True)
        self.m_grid6.EnableGridLines(True)
        self.m_grid6.EnableDragGridSize(False)
        self.m_grid6.SetMargins(0, 0)

        # Columns
        self.m_grid6.SetColSize(0, 120)
        self.m_grid6.SetColSize(1, 150)
        self.m_grid6.SetColSize(2, 120)
        self.m_grid6.SetColSize(3, 120)
        self.m_grid6.SetColSize(4, 90)
        self.m_grid6.EnableDragColMove(False)
        self.m_grid6.EnableDragColSize(True)
        self.m_grid6.SetColLabelSize(45)
        self.m_grid6.SetColLabelValue(0, u"Date")
        self.m_grid6.SetColLabelValue(1, u"ID Tabel")
        self.m_grid6.SetColLabelValue(2, u"Nama Tabel")
        self.m_grid6.SetColLabelValue(3, u"Start row")
        self.m_grid6.SetColLabelValue(4, u"End row")
        self.m_grid6.SetColLabelValue(5, u"row count")
        self.m_grid6.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid6.EnableDragRowSize(True)
        self.m_grid6.SetRowLabelSize(80)
        self.m_grid6.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid6.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer13.Add(self.m_grid6, 0, wx.ALL, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_buttonETL = wx.Button(self.m_panel6, wx.ID_ANY, u"Extract Data", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.m_buttonETL, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(self.m_panel6, wx.ID_ANY, u"Load Data", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self.m_panel6, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.m_button5, 0, wx.ALL, 5)


        bSizer13.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer12.Add(bSizer13, 1, wx.EXPAND, 5)

        self.m_panel6.SetSizer(bSizer12)
        self.m_panel6.Layout()
        bSizer12.Fit(self.m_panel6)
        self.m_notebook1.AddPage(self.m_panel6, u"ETL", True)
        self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer41 = wx.BoxSizer(wx.VERTICAL)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText5.Wrap(-1)
        bSizer8.Add(self.m_staticText5, 0, wx.ALL, 5)

        m_tahunChoices = [u"2018", u"2017", u"2016"]
        self.m_tahun = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_tahunChoices, 0)
        self.m_tahun.SetSelection(0)
        bSizer8.Add(self.m_tahun, 0, wx.ALL, 5)

        bSizer7.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Semester", wx.DefaultPosition, wx.Size(200, -1),
                                           0)
        self.m_staticText6.Wrap(-1)
        bSizer9.Add(self.m_staticText6, 0, wx.ALL, 5)

        m_semesterChoices = [u"Ganjil", u"Genap", u"Pendek", u"Remidi"]
        self.m_semester = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_semesterChoices,
                                    0)
        self.m_semester.SetSelection(0)
        bSizer9.Add(self.m_semester, 0, wx.ALL, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button1, 0, wx.ALL, 5)

        bSizer41.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid2 = wx.grid.Grid(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(900, 500), 0)

        # Grid
        self.m_grid2.CreateGrid(10, 3)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(20, 20)

        # Columns
        self.m_grid2.SetColSize(0, 189)
        self.m_grid2.SetColSize(1, 156)
        self.m_grid2.SetColSize(2, 222)
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelValue(0, u"Matakuliah")
        self.m_grid2.SetColLabelValue(1, u"SKS")
        self.m_grid2.SetColLabelValue(2, u"Jumlah Mahasiswa")
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer5.Add(self.m_grid2, 0, wx.ALL, 5)

        bSizer41.Add(bSizer5, 1, wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer41)
        self.m_panel1.Layout()
        self.m_notebook1.AddPage(self.m_panel1, u"Laporan Mahasiswa", False)
        self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.Size(1200, 900), wx.TAB_TRAVERSAL)
        bSizer411 = wx.BoxSizer(wx.VERTICAL)

        bSizer71 = wx.BoxSizer(wx.VERTICAL)

        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText51 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Tahun", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_staticText51.Wrap(-1)
        bSizer81.Add(self.m_staticText51, 0, wx.ALL, 5)

        m_tahun1Choices = [u"2018", u"2017", u"2016"]
        self.m_tahun1 = wx.Choice(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_tahun1Choices, 0)
        self.m_tahun1.SetSelection(0)
        bSizer81.Add(self.m_tahun1, 0, wx.ALL, 5)

        bSizer71.Add(bSizer81, 1, wx.EXPAND, 5)

        bSizer91 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText61 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Semester", wx.DefaultPosition, wx.Size(200, -1),
                                            0)
        self.m_staticText61.Wrap(-1)
        bSizer91.Add(self.m_staticText61, 0, wx.ALL, 5)

        m_semester1Choices = [u"Ganjil", u"Genap", u"Pendek", u"Remidi"]
        self.m_semester1 = wx.Choice(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_semester1Choices,
                                     0)
        self.m_semester1.SetSelection(0)
        bSizer91.Add(self.m_semester1, 0, wx.ALL, 5)

        bSizer71.Add(bSizer91, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText52 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Masukkan NIM", wx.DefaultPosition,
                                            wx.Size(200, -1), 0)
        self.m_staticText52.Wrap(-1)
        bSizer13.Add(self.m_staticText52, 0, wx.ALL, 5)

        self.m_inputnim = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        bSizer13.Add(self.m_inputnim, 0, wx.ALL, 5)

        bSizer71.Add(bSizer13, 1, wx.EXPAND, 5)

        self.m_button2 = wx.Button(self.m_panel2, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer71.Add(self.m_button2, 0, wx.ALL, 5)

        bSizer411.Add(bSizer71, 1, wx.EXPAND, 5)

        bSizer51 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid3 = wx.grid.Grid(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid3.CreateGrid(10, 5)
        self.m_grid3.EnableEditing(True)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(20, 20)

        # Columns
        self.m_grid3.SetColSize(0, 180)
        self.m_grid3.SetColSize(1, 120)
        self.m_grid3.SetColSize(2, 130)
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelValue(0, u"Kode Matakuliah")
        self.m_grid3.SetColLabelValue(1, u"Matakuliah")
        self.m_grid3.SetColLabelValue(2, u"SKS")
        self.m_grid3.SetColLabelValue(3, u"Indeks")
        self.m_grid3.SetColLabelValue(4, u"Nilai")
        self.m_grid3.SetColLabelValue(5, wx.EmptyString)
        self.m_grid3.SetColLabelValue(6, u"Indeks")
        self.m_grid3.SetColLabelValue(7, wx.EmptyString)
        self.m_grid3.SetColLabelValue(8, wx.EmptyString)
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(80)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer51.Add(self.m_grid3, 0, wx.ALL, 5)

        bSizer411.Add(bSizer51, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText62 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Indeks Prestasi Semester (IPS)",
                                            wx.DefaultPosition, wx.Size(300, -1), 0)
        self.m_staticText62.Wrap(-1)
        bSizer15.Add(self.m_staticText62, 0, wx.ALL, 5)

        self.m_textIPS = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.m_textIPS, 0, wx.ALL, 5)

        bSizer14.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer17 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Indeks Prestasi Kumulatif (IPK)",
                                           wx.DefaultPosition, wx.Size(300, -1), 0)
        self.m_staticText8.Wrap(-1)
        bSizer17.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_textIPK = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer17.Add(self.m_textIPK, 0, wx.ALL, 5)

        bSizer14.Add(bSizer17, 1, wx.EXPAND, 5)

        bSizer411.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer411)
        self.m_panel2.Layout()
        self.m_notebook1.AddPage(self.m_panel2, u"Laporan KHS", True)

        bSizer4.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()
        self.m_menubar3 = wx.MenuBar(0)
        self.m_menu4 = wx.Menu()
        self.m_menuETL = wx.MenuItem(self.m_menu4, wx.ID_ANY, u"Proses ETL", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.AppendItem(self.m_menuETL)

        self.m_menubar3.Append(self.m_menu4, u"Option")

        self.m_menu5 = wx.Menu()
        self.m_menuExit = wx.MenuItem(self.m_menu5, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu5.AppendItem(self.m_menuExit)
        self.m_menubar3.Append(self.m_menu5, u"Exit")

        self.SetMenuBar(self.m_menubar3)

        self.Centre(wx.BOTH)
        # self.Bind(wx.EVT_MENU, self.on_click_menu_etl, self.m_menuETL)
        self.Bind(wx.EVT_MENU, self.onExit, self.m_menuExit)

        self.m_button1.Bind(wx.EVT_BUTTON, self.submit)
        self.m_button2.Bind(wx.EVT_BUTTON, self.lihat)
        self.m_buttonETL.Bind(wx.EVT_BUTTON, self.etl_test)
        self.m_button4.Bind(wx.EVT_BUTTON, self.onClick_test)
        self.m_button5.Bind(wx.EVT_BUTTON,self.onLoad)


    def __del__(self):
        pass

    def etl_test(self,event):
        history.main()
        pass

    def onClick_test(self,event):
        tahun = self.m_choice7.GetStringSelection()
        mycursor = mydb2.cursor()
        sql = "SELECT update_log.`date`,master_id,master_name,start_row,end_row FROM update_log WHERE YEAR(date)='" + tahun + "' ORDER BY id DESC LIMIT 10"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for i in range(0, len(rows)):
            for j in range(0, len(rows[i])):
                self.m_grid6.SetCellValue(i, j, str(rows[i][j]))

    def onLoad(self,event):
        self.m_grid6.ClearGrid()
        history.main()
        pass

    def onExit(self,event):
        self.Close()

    def __del__(self):
        pass


    def submit(self,event):
        self.m_grid2.ClearGrid()
        tahun = self.m_tahun.GetStringSelection()
        semester = self.m_semester.GetStringSelection()
        if semester == 'Ganjil':
            semester = 1
        elif semester == 'Genap':
            semester = 2
        elif semester == 'Pendek':
            semester = 3
        else:
            semester = 'Remidi'
        mycursor = mydb2.cursor()
        sql = "SELECT nama_matkul,sks,COUNT(nama_mhs) AS total FROM fact_krs INNER JOIN dim_matkul USING (id_matkul)" \
              "INNER JOIN dim_mahasiswa USING (id_mhs) INNER JOIN dim_semester USING (id_semester) " \
              "WHERE id_semester = '"+str(semester)+"' && YEAR(tahun_ajaran)='"+tahun+"' GROUP BY nama_matkul"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        for i in range(0, len(rows)):
            for j in range(0, len(rows[i])):
                self.m_grid2.SetCellValue(i, j, str(rows[i][j]))

    def lihat(self, event):
        self.m_grid3.ClearGrid()
        tahun = self.m_tahun.GetStringSelection()
        semester = self.m_semester.GetStringSelection()
        total_nilai = 0
        total_sks = 0

        # ipk = self.m_textIPK.AppendText()
        if semester == 'Ganjil':
            semester = 1
        elif semester == 'Genap':
            semester = 2
        elif semester == 'Pendek':
            semester = 3
        else:
            semester = 'Remidi'
        mycursor = mydb2.cursor()
        sql = "SELECT dim_matkul.kode_matkul,nama_matkul,sks,indeks,nilai FROM fact_khs INNER JOIN dim_matkul USING (id_matkul) " \
              "INNER JOIN dim_semester USING (id_semester) INNER JOIN dim_mahasiswa USING (id_mhs) WHERE id_semester ='" + str(
            semester) + "' && YEAR(tahun_ajaran)='" + tahun + "' && NIM LIKE '%" + self.m_inputnim.Value + "%'"
        mycursor.execute(sql)

        rows = mycursor.fetchall()
        for i in range(0, len(rows)):
            total_nilai = total_nilai + rows[i][4]
            total_sks = total_sks + rows[i][2]
            for j in range(0, len(rows[i])):
                self.m_grid3.SetCellValue(i, j, str(rows[i][j]))
        self.m_inputnim.SetFocus()
        self.m_textIPS.Clear()
        self.m_textIPK.Clear()
        self.m_textIPS.AppendText("%.2f" % (total_nilai / total_sks))

        ipk = "SELECT IPK FROM fact_khs INNER JOIN dim_semester USING(id_semester) " \
              "INNER JOIN dim_mahasiswa USING (id_mhs) WHERE id_semester ='" + str(
            semester) + "' && YEAR(tahun_ajaran)='" + tahun + "' && NIM LIKE '%" + self.m_inputnim.Value + "%'"
        mycursor.execute(ipk)
        a = mycursor.fetchone()
        self.m_textIPK.AppendText("%.2f" %(a[0]))


class MainApp(wx.App):
 def OnInit(self):
  mainFrame = MyFrame1(None)
  mainFrame.Show(True)
  return True

if __name__ == '__main__':
 app = MainApp()
 app.MainLoop()

mxd=arcpy.mapping.MapDocument("CURRENT")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  mxd.dataDrivenPages.currentPageID = pageNum
  pageName=mxd.dataDrivenPages.pageRow.SUPER_NO_2016
  pageShy=mxd.dataDrivenPages.pageRow.Ssec_Name
  arcpy.mapping.ExportToJPEG(mxd, r"E:\Temp Share (E)\Temp_JPG\L\L"+"_" + pageShy +" _ " + pageName +".JPG")
del mxd



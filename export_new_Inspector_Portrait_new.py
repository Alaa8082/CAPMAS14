
mxd=arcpy.mapping.MapDocument("CURRENT")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  mxd.dataDrivenPages.currentPageID = pageNum
  pageName=mxd.dataDrivenPages.pageRow.ins_code
  pageShy=mxd.dataDrivenPages.pageRow.Ssec_Name
  arcpy.mapping.ExportToJPEG(mxd, r"E:\Temp Share (E)\Temp_JPG\P\P"+"_" + pageShy +" _Ins_ " + pageName +".JPG")
del mxd



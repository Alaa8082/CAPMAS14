
>>> 
... mxd=arcpy.mapping.MapDocument("CURRENT")
... for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
...   mxd.dataDrivenPages.currentPageID = pageNum
...   pageName=mxd.dataDrivenPages.pageRow.SUPER_NO_2016
...   pageShy=mxd.dataDrivenPages.pageRow.Ssec_Name
...   pageEA=mxd.dataDrivenPages.pageRow.EA_num
...   arcpy.mapping.ExportToJPEG(mxd, r"F:\Work\CAPMAS\work census\Temp_JPG\P\P"+"_" + pageShy +" _ " + pageName + " _ " + pageEA +".JPG")
... del mxd
... 
... 
... 

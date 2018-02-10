Attribute VB_Name = "Module1"
Sub Ticker():

Dim Current As Worksheet

For Each Current In ActiveWorkbook.Worksheets

    Dim i As Double

    Dim tickerrow As Double
    tickerrow = 2

    Dim totalrow As Double
    totalrow = 2

    Dim stockvol As Double
    stockvol = 0

    Dim opencell As Double
    opencell = 0

    Dim stockdiff As Long
    stockdiff = 2
    
    Dim stockpercent As Long
    stockpercent = 2

    'Dim maxstock As Double
    'maxstock = 0
    
    Dim j As Integer
    Dim max As Double
    Dim min As Double
    Dim totalmaxstock As Double

    max = 0
    min = 0
    totalmaxstock = 0
    
    Cells(1, 9).Value = "Ticker Name"
    Cells(1, 10).Value = "Total Stock Volume"
    Cells(1, 11).Value = "Difference in price"
    Cells(1, 12).Value = "Percentage difference"
    
    For i = 2 To 797711
    
    
        Cells(totalrow, 9).Value = stockvol
    
        If (Cells(i + 1, 1).Value <> Cells(i, 1).Value) Then
    
                'Gives Ticker Name
                Cells(tickerrow, 9).Value = Cells(i, 1).Value
                Cells(tickerrow + 1, 9).Value = Cells(i + 1, 1).Value
                tickerrow = tickerrow + 1
            
                'Gives respective stock vol sum
                stockvol = stockvol + Cells(i, 7).Value
                Cells(totalrow, 10).Value = stockvol
                totalrow = totalrow + 1
            
                stockvol = 0
                
                If (Cells(i, 2).Value = "PLNT") Then
                    'Gives difference in opening and closing values
                    Cells(stockdiff, 11).Value = Cells(i, 6).Value - opencell
                    Cells(stockdiff, 12).Value = 0
                Else
                    Cells(stockdiff, 11).Value = Cells(i, 6).Value - opencell
                    Cells(stockdiff, 12).Value = ((Cells(i, 6).Value - opencell) / opencell)
                End If
                
                'Colors cell interiors
                If (Cells(stockdiff, 11).Value > 0) Then
                    Cells(stockdiff, 11).Interior.ColorIndex = 4
                Else
                    Cells(stockdiff, 11).Interior.ColorIndex = 3
            
                End If
                
                stockdiff = stockdiff + 1
            
                opencell = Cells(i + 1, 3).Value
            
          
        ElseIf (i = 2) Then
            
                'hard codes initial value of opening stock
                opencell = Cells(2, 3).Value
            
                stockvol = stockvol + Cells(i, 3).Value
           
        Else
        
                stockvol = stockvol + Cells(i, 7).Value
            
        End If
    
    
    Next i


Next


End Sub

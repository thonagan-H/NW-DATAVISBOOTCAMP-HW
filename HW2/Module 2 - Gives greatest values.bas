Attribute VB_Name = "Module2"
Sub greatest():

    Dim j As Integer
    Dim max As Double
    Dim min As Double
    Dim totalmaxstock As Double

    max = 0
    min = 0
    totalmaxstock = 0

For j = 2 To 10000
    
    Cells(j, 12).NumberFormat = "0.00000%"
    Cells(2, 16).NumberFormat = "0.00000%"
    Cells(3, 16).NumberFormat = "0.00000%"
    If (Cells(j, 12).Value > max) Then
        
        max = Cells(j, 12).Value
        Cells(2, 14).Value = "Greatest % increase"
        Cells(2, 15).Value = Cells(j, 9).Value
        Cells(2, 16).Value = max
    End If
    
    If (Cells(j, 12).Value < min) Then
        
        min = Cells(j, 12).Value
        Cells(3, 14).Value = "Greatest % decrease"
        Cells(3, 15).Value = Cells(j, 9).Value
        Cells(3, 16).Value = min
        
    End If
    
    If (Cells(j, 10).Value > totalmaxstock) Then
        
        totalmaxstock = Cells(j, 10).Value
        Cells(4, 14).Value = "Greatest value of total stock"
        Cells(4, 15).Value = Cells(j, 9).Value
        Cells(4, 16).Value = totalmaxstock
    
    End If

Next j

End Sub

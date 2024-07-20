from rest_framework.response import Response
from rest_framework import generics, status
from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceItemSerializer

class InvoiceView(generics.GenericAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get(self, request):
        invoices = self.get_queryset()
        serializer = self.get_serializer(invoices, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        return Response({"message":"Updated Invoice!"})
    
    def delete(self, request):
        return Response({"message":"Deleted Invoice!"})
    

class InvoiceItemView(generics.GenericAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

    def get_queryset(self):
        invoice_id = self.kwargs.get('invoice_id')
        return InvoiceItem.objects.filter(invoiceID=invoice_id)

    def get(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        return Response({"message":"Added a new item to Invoice!"})
    
    def patch(self, request):
        return Response({"message":"Updated an Invoice item!"})
    
    def delete(self, request):
        return Response({"message":"Deleted an Invoice item!"})


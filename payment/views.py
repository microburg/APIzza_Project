# payment/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def process_payment(request):
    # بيانات الدفع الواردة من React
    card_number = request.data.get('card_number')
    expiry_date = request.data.get('expiry_date')
    cvv = request.data.get('cvv')
    phone_number = request.data.get('phone_number')
    amount = request.data.get('amount')

    # معالجة الدفع (مثال بسيط: قبول الدفع)
    return Response({"success": True, "message": "Payment processed successfully!"})

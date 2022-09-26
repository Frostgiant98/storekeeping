from rest_framework import serializers

from .models import Item, Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name', 'store_id']



class ItemSerializer(serializers.ModelSerializer):

    store = StoreSerializer(many = False, read_only = True)   

    class Meta:
        model = Item
        fields = ['item_name','quantity','expiry_date','entry_date','store']


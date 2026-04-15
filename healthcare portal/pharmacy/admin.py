from django.contrib import admin
from .models import Medicine, MedicineCategory, Dispensing, StockMovement

# Register your models here.

admin.site.register(Medicine)
admin.site.register(MedicineCategory)
admin.site.register(Dispensing)
admin.site.register(StockMovement)

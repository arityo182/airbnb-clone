from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definiton"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book ")},
        ),
        (
            "Spaces",
            {"fields": ("guest", "beds", "bedrooms", "baths")},
        ),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    ordering = (
        "name",
        "price",
        "bedrooms",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rule")

    def count_amenities(self, obj):
        print(obj.amenities.all())
        return "Potato"

    count_amenities.short_description = "Hello!"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """"""

    pass

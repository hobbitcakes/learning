from django.contrib import admin

from .models import Game, Move

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status', )

admin.site.register(Move)

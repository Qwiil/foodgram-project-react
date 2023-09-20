from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag)


class IngredientAdmin(admin.ModelAdmin):
    """ Админ панель управление ингредиентами """
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class IngredientInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 5
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    """Класс настройки раздела рецептов."""
    list_display = ('author', 'name', 'cooking_time',
                    'get_favorites', 'get_ingredients',)
    search_fields = ('name', 'author', 'tags')
    list_filter = ('author', 'name', 'tags')
    inlines = (IngredientInline,)
    empty_value_display = 'пусто'

    def get_favorites(self, obj):
        return obj.favorites.count()

    def get_ingredients(self, obj):
        """Получает ингредиент или список ингредиентов рецепта."""
        return ', '.join([
            ingredients.name for ingredients
            in obj.ingredients.values(
                'ingredient_name', 'amount',
                'ingredient_measurement_unit')])


class ShoppingCartAdmin(admin.ModelAdmin):
    """ Админ панель списка покупок """
    list_display = ('recipe', 'user')
    list_filter = ('recipe', 'user')
    search_fields = ('user', )
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    """ Админ панель управление тегами """
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    """ Админ панель управление подписками """
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')
    empty_value_display = 'пусто'


admin.site.register(Tag, TagAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(Ingredient, IngredientAdmin)

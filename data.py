class URL:
    base_url = 'https://foodgram-frontend-1.foodgram.education-services.ru'
    
    test_url = base_url
    login_page_url = f'{base_url}/signin'
    home_page_url = f'{base_url}/recipes'

class TestData:
    username = 'LotharXIII'
    password = '29081992!'
    recipe_name = 'Тост с сыром'
    cheese = 'сыр'
    weight = '50'
    ingredients = {'хлеб': '100','моцарелла': '50', 'сливочное масло': '10', 'зелень': '10' }
    time = '8'
    description = 'Поджарьте хлеб, смажьте один кусочек сливочным маслом, сверху положите сыр, накройте вторым кусочком хлеба и запекайте в гриле до готовности'
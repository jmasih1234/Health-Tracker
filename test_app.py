import pytest
from app import app, DefiningCondition
from nutritionPlanner import nutrition_health, calculate_macros


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestNutritionPlanner:
    """Test cases for nutrition planning calculations."""
    
    def test_bmr_calculation_male(self):
        """Test BMR calculation for males using Mifflin-St Jeor formula."""
        # Test data: 25 year old male, 80kg, 180cm
        main_cal, intake_cal = nutrition_health(25, 80, 'male', 180, 'none', [], 'maintaining')
        
        # BMR = 10*80 + 6.25*180 - 5*25 + 5 = 800 + 1125 - 125 + 5 = 1805
        # Sedentary (none) = 1805 * 1.2 = 2166
        assert main_cal == pytest.approx(2166, rel=0.01)
    
    def test_bmr_calculation_female(self):
        """Test BMR calculation for females."""
        # Test data: 25 year old female, 65kg, 170cm
        main_cal, intake_cal = nutrition_health(25, 65, 'female', 170, 'none', [], 'maintaining')
        
        # BMR = 10*65 + 6.25*170 - 5*25 - 161 = 650 + 1062.5 - 125 - 161 = 1426.5
        # Sedentary (none) = 1426.5 * 1.2 = 1711.8
        assert main_cal == pytest.approx(1711.8, rel=0.01)
    
    def test_activity_level_little(self):
        """Test activity level multiplier for lightly active."""
        main_cal, _ = nutrition_health(30, 70, 'male', 175, 'little', [], 'maintaining')
        
        # BMR = 10*70 + 6.25*175 - 5*30 + 5 = 700 + 1093.75 - 150 + 5 = 1648.75
        # Little active = 1648.75 * 1.375 = 2267.03
        assert main_cal == pytest.approx(2267.03, rel=0.01)
    
    def test_activity_level_moderate(self):
        """Test activity level multiplier for moderately active."""
        main_cal, _ = nutrition_health(30, 70, 'male', 175, 'moderate', [], 'maintaining')
        
        # BMR = 1648.75
        # Moderate = 1648.75 * 1.55 = 2555.5625
        assert main_cal == pytest.approx(2555.5625, rel=0.01)
    
    def test_activity_level_very_active(self):
        """Test activity level multiplier for very active."""
        main_cal, _ = nutrition_health(30, 70, 'male', 175, 'very active', [], 'maintaining')
        
        # BMR = 1648.75
        # Very active = 1648.75 * 1.725 = 2844.09
        assert main_cal == pytest.approx(2844.09, rel=0.01)
    
    def test_activity_level_extra_active(self):
        """Test activity level multiplier for extra active."""
        main_cal, _ = nutrition_health(30, 70, 'male', 175, 'extra active', [], 'maintaining')
        
        # BMR = 1648.75
        # Extra active = 1648.75 * 1.94 = 3198.575
        assert main_cal == pytest.approx(3198.575, rel=0.01)
    
    def test_goal_bulking(self):
        """Test bulking goal adds 500 calories."""
        main_cal, intake_cal = nutrition_health(30, 70, 'male', 175, 'moderate', [], 'bulking')
        
        # Maintenance is 2555.5625, bulking adds 500
        assert intake_cal == pytest.approx(main_cal + 500, rel=0.01)
    
    def test_goal_cutting(self):
        """Test cutting goal subtracts 500 calories."""
        main_cal, intake_cal = nutrition_health(30, 70, 'male', 175, 'moderate', [], 'cutting')
        
        # Maintenance is 2555.5625, cutting subtracts 500
        assert intake_cal == pytest.approx(main_cal - 500, rel=0.01)
    
    def test_goal_maintaining(self):
        """Test maintaining goal keeps calories at maintenance."""
        main_cal, intake_cal = nutrition_health(30, 70, 'male', 175, 'moderate', [], 'maintaining')
        
        # Maintenance should equal intake for maintaining goal
        assert intake_cal == pytest.approx(main_cal, rel=0.01)


class TestMacroCalculations:
    """Test cases for macro nutrient calculations."""
    
    def test_macro_calculation_2000_calories(self):
        """Test macro calculation with 2000 calories."""
        P, C, F = calculate_macros(2000)
        
        # Protein: 2000/4 * 0.35 = 175g
        # Carbs: 2000/4 * 0.4 = 200g
        # Fats: 2000/9 * 0.25 = 55.56g
        assert P == pytest.approx(175, rel=0.01)
        assert C == pytest.approx(200, rel=0.01)
        assert F == pytest.approx(55.56, rel=0.01)
    
    def test_macro_calculation_2500_calories(self):
        """Test macro calculation with 2500 calories."""
        P, C, F = calculate_macros(2500)
        
        # Protein: 2500/4 * 0.35 = 218.75g
        # Carbs: 2500/4 * 0.4 = 250g
        # Fats: 2500/9 * 0.25 = 69.44g
        assert P == pytest.approx(218.75, rel=0.01)
        assert C == pytest.approx(250, rel=0.01)
        assert F == pytest.approx(69.44, rel=0.01)
    
    def test_macro_ratios(self):
        """Test that macros maintain correct calorie ratios."""
        intake_cal = 2000
        P, C, F = calculate_macros(intake_cal)
        
        # Calculate back to calories
        cal_from_protein = P * 4
        cal_from_carbs = C * 4
        cal_from_fats = F * 9
        total_cal = cal_from_protein + cal_from_carbs + cal_from_fats
        
        # Should be approximately 2000 calories
        assert total_cal == pytest.approx(intake_cal, rel=0.01)


class TestDefiningCondition:
    """Test cases for health condition definitions."""
    
    def test_has_anorexia(self):
        """Test anorexia condition handler."""
        condition = DefiningCondition()
        condition.has_anorexia()
        assert condition.anorexia is True
    
    def test_has_diabetes(self):
        """Test diabetes condition handler."""
        condition = DefiningCondition()
        condition.has_diabetes()
        assert condition.diabetes is True
    
    def test_has_heart_disease(self):
        """Test heart disease condition handler."""
        condition = DefiningCondition()
        condition.has_heart_disease()
        assert condition.heart_disease is True
    
    def test_has_cancer(self):
        """Test cancer condition handler."""
        condition = DefiningCondition()
        condition.has_cancer()
        assert condition.cancer is True
    
    def test_has_arthritis(self):
        """Test arthritis condition handler."""
        condition = DefiningCondition()
        condition.has_arthritis()
        assert condition.arthritis is True
    
    def test_multiple_conditions(self):
        """Test setting multiple conditions."""
        condition = DefiningCondition()
        condition.has_diabetes()
        condition.has_heart_disease()
        
        assert condition.diabetes is True
        assert condition.heart_disease is True
        assert condition.anorexia is False


class TestFlaskApp:
    """Test cases for Flask app routes and functionality."""
    
    def test_index_get(self, client):
        """Test GET request to index page."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Health Tracker' in response.data
        assert b'Personal Information' in response.data
    
    def test_index_get_has_form_fields(self, client):
        """Test that form fields are present on index page."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'age' in response.data
        assert b'weight' in response.data
        assert b'height' in response.data
        assert b'gender' in response.data
        assert b'activity' in response.data
    
    def test_index_post_with_valid_data(self, client):
        """Test POST request with valid form data."""
        response = client.post('/', data={
            'age': '25',
            'weight': '80',
            'gender': 'male',
            'height': '180',
            'activity': 'moderate',
            'goals': 'maintaining'
        })
        
        assert response.status_code == 200
        assert b'Your Personalized Plan' in response.data or b'Results' in response.data.lower()
    
    def test_index_post_bulking(self, client):
        """Test POST request with bulking goal."""
        response = client.post('/', data={
            'age': '30',
            'weight': '75',
            'gender': 'male',
            'height': '175',
            'activity': 'moderate',
            'goals': 'bulking'
        })
        
        assert response.status_code == 200
        # Should show results
        assert b'Bulking' in response.data or b'calories' in response.data.lower()
    
    def test_index_post_cutting(self, client):
        """Test POST request with cutting goal."""
        response = client.post('/', data={
            'age': '30',
            'weight': '75',
            'gender': 'male',
            'height': '175',
            'activity': 'moderate',
            'goals': 'cutting'
        })
        
        assert response.status_code == 200
        assert b'Cutting' in response.data or b'calories' in response.data.lower()
    
    def test_index_post_with_conditions(self, client):
        """Test POST request with health conditions."""
        response = client.post('/', data={
            'age': '40',
            'weight': '85',
            'gender': 'male',
            'height': '180',
            'activity': 'little',
            'conditions': ['Diabetes', 'Heart Disease'],
            'goals': 'maintaining'
        })
        
        assert response.status_code == 200
    
    def test_index_post_female(self, client):
        """Test POST request for female user."""
        response = client.post('/', data={
            'age': '28',
            'weight': '65',
            'gender': 'female',
            'height': '170',
            'activity': 'moderate',
            'goals': 'cutting'
        })
        
        assert response.status_code == 200
        assert b'Your Personalized Plan' in response.data or b'calories' in response.data.lower()
    
    def test_index_post_returns_results(self, client):
        """Test that POST request returns macro and calorie results."""
        response = client.post('/', data={
            'age': '25',
            'weight': '70',
            'gender': 'male',
            'height': '175',
            'activity': 'moderate',
            'goals': 'maintaining'
        })
        
        assert response.status_code == 200
        # Check for calorie and macro-related text
        response_text = response.data.decode().lower()
        assert 'calor' in response_text or 'protein' in response_text or 'carbs' in response_text


class TestIntegration:
    """Integration tests for the entire app workflow."""
    
    def test_full_workflow_male_bulking(self, client):
        """Test complete workflow for male user trying to bulk."""
        # Submit form
        response = client.post('/', data={
            'age': '25',
            'weight': '80',
            'gender': 'male',
            'height': '180',
            'activity': 'very active',
            'conditions': ['Diabetes'],
            'goals': 'bulking'
        })
        
        assert response.status_code == 200
        response_text = response.data.decode()
        
        # Verify results are displayed
        assert 'Health Tracker' in response_text
    
    def test_full_workflow_female_cutting(self, client):
        """Test complete workflow for female user trying to cut."""
        response = client.post('/', data={
            'age': '30',
            'weight': '65',
            'gender': 'female',
            'height': '168',
            'activity': 'moderate',
            'conditions': [],
            'goals': 'cutting'
        })
        
        assert response.status_code == 200
        response_text = response.data.decode()
        assert 'Health Tracker' in response_text
    
    def test_full_workflow_no_conditions(self, client):
        """Test workflow with no health conditions selected."""
        response = client.post('/', data={
            'age': '35',
            'weight': '75',
            'gender': 'male',
            'height': '180',
            'activity': 'extra active',
            'goals': 'maintaining'
        })
        
        assert response.status_code == 200


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

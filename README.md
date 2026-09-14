# Health Tracker - Nutrition & Workout Planner

A modern, responsive web application that provides personalized nutrition and workout plans based on user health profiles.

## Features

✨ **Modern Design**
- Clean, minimal UI built with Tailwind CSS
- Fully responsive design (mobile, tablet, desktop)
- Smooth interactions and visual feedback

📊 **Nutrition Planning**
- Accurate BMR (Basal Metabolic Rate) calculation using Mifflin-St Jeor formula
- Activity level customization (Sedentary to Extra Active)
- Personalized macro nutrient calculations (Protein, Carbs, Fats)
- Three fitness goals: Cutting, Maintaining, Bulking

💪 **Health Condition Support**
- Anorexia guidance and dietary recommendations
- Diabetes management support
- Heart disease considerations
- Cancer recovery support
- Arthritis-friendly workout plans
- Obesity management

🎯 **User-Friendly Interface**
- Intuitive form with organized sections
- Color-coded fitness goals (visual selector)
- Clear results display with calorie breakdowns
- Professional typography and spacing

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Testing**: pytest
- **Deployment**: GitHub

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Health-Tracker.git
cd Health-Tracker
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Development Server

```bash
python3 app.py
```

The application will be available at `http://127.0.0.1:5000`

### Running Tests

```bash
python3 -m pytest test_app.py -v
```

## Project Structure

```
Health-Tracker/
├── app.py                    # Flask application and routes
├── nutritionPlanner.py       # Nutrition calculations
├── conditions.py             # Health condition information
├── workoutPlanner.py         # Workout plan generation
├── main.py                   # CLI interface
├── test_app.py               # Comprehensive unit tests
├── templates/
│   └── index.html            # Main web interface
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Usage

1. Open the web application in your browser
2. Fill in your personal information:
   - Age, weight, height, gender
   - Activity level (Sedentary to Extra Active)
3. Select any applicable health conditions
4. Choose your fitness goal (Cutting/Maintaining/Bulking)
5. Click "Generate My Plan"
6. View your personalized results:
   - Daily calorie targets
   - Macro nutrient breakdown (Protein, Carbs, Fats)
   - Condition-specific recommendations

## Testing

The application includes **29 comprehensive unit tests** covering:

- ✅ BMR calculations for males and females
- ✅ Activity level multipliers
- ✅ Fitness goal adjustments (bulking, cutting, maintaining)
- ✅ Macro nutrient calculations
- ✅ Health condition handling
- ✅ Flask app routes and form submission
- ✅ Full workflow integration tests

**Test Results**: All 29 tests passing ✓

```bash
python3 -m pytest test_app.py -v
# Output: 29 passed in 0.13s
```

## Recent Updates

- ✅ Fixed circular import in nutritionPlanner.py
- ✅ Fixed goal mapping ("bulk"→"bulking", "cut"→"cutting")
- ✅ Added "maintaining" goal support
- ✅ Fixed health_conditions template passing
- ✅ Modernized UI with Tailwind CSS
- ✅ Added comprehensive unit tests
- ✅ Ready for GitHub deployment

## Disclaimer

This application provides general nutritional guidance and is not a substitute for professional medical or dietary advice. Always consult with qualified healthcare providers, nutritionists, or trainers before making significant changes to your diet or exercise routine.

---

**Built with ❤️ for health tracking**

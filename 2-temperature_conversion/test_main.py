from main import convertCelsiusToFahrenheit, convertFahrenheitToCelsius

def test_convertCelsiusToFahrenheit():
    assert convertCelsiusToFahrenheit(10) == 50
    assert convertCelsiusToFahrenheit(0) == 32
    assert convertCelsiusToFahrenheit(100) == 212

def test_convertFahrenheitToCelsius():
    assert convertFahrenheitToCelsius(0) == -17.77777777777778
    assert convertFahrenheitToCelsius(180) == 82.22222222222223
    assert convertFahrenheitToCelsius(convertCelsiusToFahrenheit(15)) == 15

# Run the tests
test_convertCelsiusToFahrenheit()
test_convertFahrenheitToCelsius()
import nose
from temperature import to_celsius, above_freezing

def test_freezing():
  assert to_celsius(32) == 0
  
def test_boiling():
  assert to_celsius(212) == 100
  
def test_round():
  assert to_celsius(100) == 38, 'returning an unrounded result'

def test_above_freezing():
  assert above_freezing(89.4), 'a temperature above freezing'
  assert not above_freezing(-42), 'a temperature below freezing'
  assert not above_freezing(0), 'a temperature at freezing is not above'

if __name__ == '__main__':
  nose.runmodule()

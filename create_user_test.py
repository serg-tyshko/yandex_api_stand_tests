import sender_stand_request
import data


def get_kit_body(kit_name):
    kit_name_test = data.kit_body.copy()
    kit_name_test["name"] = kit_name
    return kit_name_test

# Функция для позитивной проверки
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_assert_empty(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

def negative_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    n_response = sender_stand_request.post_new_client_kit(kit_body)
    assert n_response == 400

# Test 1
def test1_dopustimoe_kolichestvo_simvolov_1():
    positive_assert("в")

# Test 2
def test2_dopustimoe_kolichestvo_simvolov_511():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )
# Test 3
def test3_kolichestvo_simvolov_menshe_dopustimogo_0():
    negative_assert("")
# Test 4
def test4_kolichestvo_simvolov_bolshe_dopustimogo_512():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Test 5
def test5_angliskie_bukvy_():
    positive_assert("QWErty")
# Test 6
def test6_russkie_bukvy_():
    positive_assert("Мария")
# Test 7
def test7_razreshen_specsimbol():
    positive_assert('"№%@"')
# Test 8
def test8_razreshen_probel():
    positive_assert('Человек и КО')
# Test 9
def test8_razreshen_chislo():
    positive_assert('123')
# Test 10
def test10_parametr_ne_peredan():
    kit_bod = data.kit_body.copy()
    kit_bod.pop("name")
    negative_assert_empty(kit_bod)
# Test 11
def test11_peredan_drugoy_tip():
    negative_assert(124)
#

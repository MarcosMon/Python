def to_camel_case(text):
    text=text.replace("-", " ").replace("_", " ")
    primera=text.find(" ")
    text1=text[primera:].title()
    text=text.replace(" ", "")
    text1=text1.replace(" ", "")
    return text[0:primera] + text1



if __name__ == '__main__':

    assert to_camel_case('') == ''
    assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
    assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
    assert to_camel_case("A-B-C") == "ABC"
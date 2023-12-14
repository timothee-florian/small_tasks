line = 'Ich möÖchte die Qualität des Produkts überprüfen, bevor ich es kaufe.'

special_char_map = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}
print(line.lower().translate(special_char_map))
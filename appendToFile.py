appendMe = 'Some text'

saveFile = open('exampleFile.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()
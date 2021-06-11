rgb = {'R':255, 'G':255, 'B':0}

def which_color (color):
    identificador = [False,False,False,False,False,False]        
    if color['R'] > 0 and color['R'] <= 255:
        identificador[0] = True
    if color['G'] > 0 and color['G'] <= 255:
        identificador[1] = True
    if color['B'] > 0 and color['B'] <= 255:
        identificador[2] = True
    
    if identificador[0] and identificador[1]:
        identificador[3] = True
    if identificador[1] and identificador[2]:
        identificador[4] = True
    if identificador[0] and identificador[2]:
        identificador[5] = True
    
    return identificador

if __name__ == '__main__':
    print(which_color(rgb))
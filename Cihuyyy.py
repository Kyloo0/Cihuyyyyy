print ('''>>==========================<<
||                     	    ||
|| Welcome to Interrogation ||
||                     	    ||
>>==========================<<'''
)

# Meembuat conditional
x = input('Mulai Interogasi (Y/N)? ')

# Input mulai interogasi jika Y
if x == 'Y':
    print('Mari kita mulai interogasi')
    a = input ('Siapa namamu? ')
    b = input ('Berapa nomor NPM mu? ')

    # NPM digit
    k = b.isdigit()
    l = list(b)

    if k == True:
        # Jika NPM berbentuk angka
        count = 0
        for i in l:
            count = count+1
            
        if count == 10: 
            # Jika NPM = 10 digit
            c = input ('Apakah kamu punya motif (Y/N)? ')
            # motif
            if c == 'Y':
                d = input('Apa motif kamu tadi? ')
                e = input('Apakah kamu punya alibi (Y/N)? ')
                # Alibi
                if e == 'Y':
                    f = input('Apa alibi kamu? ')
                    print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                    {a} lumayan mencurigakan nih... ''')
                    # Lanjut Interogasi
                    print('----------------------------------------')
                    y = input ('Lanjut interogasi (Y/N)? ')
                    # Kita buat loopingnya
                    while y :
                        if y == 'Y':
                            print('----------------------------------------')
                            a = input ('Siapa namamu? ')
                            b = input ('Berapa nomor NPM mu? ')
                            k = b.isdigit()
                            l = list(b)
                            if k == True:
                                count = 0
                                for i in l:
                                    count = count+1

                                if count == 10:
                                    c = input ('Apakah kamu punya motif (Y/N)? ')
                                    if c == 'Y':
                                        d = input('Apa motif kamu tadi? ')
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                                            {a} lumayan mencurigakan nih... ''')   
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} tapi tidak memiliki alibi
                                            Wah, {a} mencurigakan nihh >:( ''')

                                    elif c == 'N':
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                                            {a} tidak terlalu mencurigakan sih''')
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                                            {a} lumayan mencurigakan nih...''')
                                        else :
                                            print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                            
                                    else :
                                        print('Seseorang harus punya motif atau tidak punya motif sama sekali!')

                                else:
                                    print('NPM harus sepanjang 10 digits!')
                            
                            else :
                                print('NPM harus berupa angka!')
                            print('----------------------------------------')
                            # kita kembalikan loopingnya
                            y = input ('Lanjut interogasi (Y/N)? ')
                            
                        elif y == 'N':
                            # Tidak melanjutkan interogasi
                            for y in range(1):
                                break
                            print('Interogasi telah selesai')
                            print('----------------------------------------')

                        else :
                            # mengisi interogasi dengan character lain
                            for y in range (1):
                                print('Input tidak valid')
                            print('----------------------------------------')
                            # kita kembalikan loopingnya
                            y = input ('Lanjut interogasi (Y/N)? ')
                            
    
                elif e == 'N':
                    # Alibi diisi N
                    print(f'''{a} dengan NPM {b} memiliki motif {d} tapi tidak memiliki alibi
                    Wah, {a} mencurigakan nihh >:( ''')
                    print('----------------------------------------')
                    y = input ('Lanjut interogasi (Y/N)? ')
                    while y:
                        if y == 'Y':
                            print('----------------------------------------')
                            a = input ('Siapa namamu? ')
                            b = input ('Berapa nomor NPM mu? ')
                            k = b.isdigit()
                            l = list(b)
                            if k == True:
                                count = 0
                                for i in l:
                                    count = count+1
                                if count == 10 :
                                    c = input ('Apakah kamu punya motif (Y/N)? ')
                                    if c == 'Y':
                                        d = input('Apa motif kamu tadi? ')
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                                            {a} lumayan mencurigakan nih... ''')   
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} memiliki motif {c} tapi tidak memiliki alibi
                                            Wah, {a} mencurigakan nihh >:( ''')

                                    elif c == 'N':
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                                            {a} tidak terlalu mencurigakan sih''')
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                                            {a} lumayan mencurigakan nih...''')
                                        else :
                                            print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                            
                                    else :
                                        print('Seseorang harus punya motif atau tidak punya motif sama sekali!')

                                else:
                                    print('NPM harus sepanjang 10 digits!')
                            
                            else :
                                print('NPM harus berupa angka!')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')

                        elif y == 'N':
                            for y in range(1):
                                break
                            print('Interogasi telah selesai')
                            print('----------------------------------------')
                        else :
                            for y in range (1):
                                print('Input tidak valid')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')
                            

            elif c == 'N':
                # Motif diisi N
                e = input('Apakah kamu punya alibi (Y/N)? ')
                if e == 'Y':
                    f = input('Apa alibi kamu? ')
                    print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                    {a} tidak terlalu mencurigakan sih''')
                    print('----------------------------------------')
                    y = input ('Lanjut interogasi (Y/N)? ')
                    while y :
                        if y == 'Y':
                            print('----------------------------------------')
                            a = input ('Siapa namamu? ')
                            b = input ('Berapa nomor NPM mu? ')
                            k = b.isdigit()
                            l = list(b)
                            if k == True:
                                count = 0
                                for i in l:
                                    count = count+1

                                if count == 10:
                                    c = input ('Apakah kamu punya motif (Y/N)? ')
                                    if c == 'Y':
                                        d = input('Apa motif kamu tadi? ')
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                                            {a} lumayan mencurigakan nih... ''')   
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} tapi tidak memiliki alibi
                                            Wah, {a} mencurigakan nihh >:( ''')

                                    elif c == 'N':
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                                            {a} tidak terlalu mencurigakan sih''')
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                                            {a} lumayan mencurigakan nih...''')
                                        else :
                                            print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                            
                                    else :
                                        print('Seseorang harus punya motif atau tidak punya motif sama sekali!')

                                else:
                                    print('NPM harus sepanjang 10 digits!')
                            
                            else :
                                print('NPM harus berupa angka!')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')
                            

                        elif y == 'N':
                            for y in range(1):
                                break
                            print('Interogasi telah selesai')
                            print('----------------------------------------')
                        else :
                            for y in range (1):
                                print('Input tidak valid')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')
                            
                elif e == 'N':
                    print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                    {a} lumayan mencurigakan nih...''')
                    print('----------------------------------------')
                    y = input ('Lanjut interogasi (Y/N)? ')
                    while y :
                        if y == 'Y':
                            print('----------------------------------------')
                            a = input ('Siapa namamu? ')
                            b = input ('Berapa nomor NPM mu? ')
                            k = b.isdigit()
                            l = list(b)
                            if k == True:
                                count = 0
                                for i in l:
                                    count = count+1

                                if count == 10:
                                    c = input ('Apakah kamu punya motif (Y/N)? ')
                                    if c == 'Y':
                                        d = input('Apa motif kamu tadi? ')
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                                            {a} lumayan mencurigakan nih... ''')   
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} tapi tidak memiliki alibi
                                            Wah, {a} mencurigakan nihh >:( ''')

                                    elif c == 'N':
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                                            {a} tidak terlalu mencurigakan sih''')
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                                            {a} lumayan mencurigakan nih...''')
                                        else :
                                            print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                            
                                    else :
                                        print('Seseorang harus punya motif atau tidak punya motif sama sekali!')

                                else:
                                    print('NPM harus sepanjang 10 digits!')
                            
                            else :
                                print('NPM harus berupa angka!')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')
                            

                        elif y == 'N':
                            for y in range(1):
                                break
                            print('Interogasi telah selesai')
                            print('----------------------------------------')
                        else :
                            for y in range (1):
                                print('Input tidak valid')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')

                else :
                    print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                    print('----------------------------------------')
                    y = input ('Lanjut interogasi (Y/N)? ')
                    while y :
                        if y == 'Y':
                            print('----------------------------------------')
                            a = input ('Siapa namamu? ')
                            b = input ('Berapa nomor NPM mu? ')
                            k = b.isdigit()
                            l = list(b)
                            if k == True:
                                count = 0
                                for i in l:
                                    count = count+1

                                if count == 10:
                                    c = input ('Apakah kamu punya motif (Y/N)? ')
                                    if c == 'Y':
                                        d = input('Apa motif kamu tadi? ')
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                                            {a} lumayan mencurigakan nih... ''')   
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} memiliki motif {d} tapi tidak memiliki alibi
                                            Wah, {a} mencurigakan nihh >:( ''')

                                    elif c == 'N':
                                        e = input('Apakah kamu punya alibi (Y/N)? ')
                                        if e == 'Y':
                                            f = input('Apa alibi kamu? ')
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                                            {a} tidak terlalu mencurigakan sih''')
                                        elif e == 'N':
                                            print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                                            {a} lumayan mencurigakan nih...''')
                                        else :
                                            print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                            
                                    else :
                                        print('Seseorang harus punya motif atau tidak punya motif sama sekali!')

                                else:
                                    print('NPM harus sepanjang 10 digits!')
                            
                            else :
                                print('NPM harus berupa angka!')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')
                            

                        elif y == 'N':
                            for y in range(1):
                                break
                            print('Interogasi telah selesai')
                            print('----------------------------------------')
                        else :
                            for y in range (1):
                                print('Input tidak valid')
                            print('----------------------------------------')
                            y = input ('Lanjut interogasi (Y/N)? ')

        
            else :
                # Motif diisi character lain
                print('Seseorang harus punya motif atau tidak punya motif sama sekali!')
                print('----------------------------------------')
                y = input ('Lanjut interogasi (Y/N)? ')
                while y :
                    if y == 'Y':
                        print('----------------------------------------')
                        a = input ('Siapa namamu? ')
                        b = input ('Berapa nomor NPM mu? ')
                        k = b.isdigit()
                        l = list(b)
                        if k == True:
                            count = 0
                            for i in l:
                                count = count+1

                            if count == 10:
                                c = input ('Apakah kamu punya motif (Y/N)? ')
                                if c == 'Y':
                                    d = input('Apa motif kamu tadi? ')
                                    e = input('Apakah kamu punya alibi (Y/N)? ')
                                    if e == 'Y':
                                        f = input('Apa alibi kamu? ')
                                        print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                                        {a} lumayan mencurigakan nih... ''')   
                                    elif e == 'N':
                                        print(f'''{a} dengan NPM {b} memiliki motif {d} tapi tidak memiliki alibi
                                        Wah, {a} mencurigakan nihh >:( ''')

                                elif c == 'N':
                                    e = input('Apakah kamu punya alibi (Y/N)? ')
                                    if e == 'Y':
                                        f = input('Apa alibi kamu? ')
                                        print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                                        {a} tidak terlalu mencurigakan sih''')
                                    elif e == 'N':
                                        print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                                        {a} lumayan mencurigakan nih...''')
                                    else :
                                        print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                            
                                else :
                                    print('Seseorang harus punya motif atau tidak punya motif sama sekali!')

                            else:
                                print('NPM harus sepanjang 10 digits!')
                            
                        else :
                            print('NPM harus berupa angka!')
                        print('----------------------------------------')
                        y = input ('Lanjut interogasi (Y/N)? ')
                            

                    elif y == 'N':
                        for y in range(1):
                            break
                        print('Interogasi telah selesai')
                        print('----------------------------------------')
                    else :
                        for y in range (1):
                            print('Input tidak valid')
                        print('----------------------------------------')
                        y = input ('Lanjut interogasi (Y/N)? ')


        else:
            # Jika NPM tidak = 10 digit
            print('NPM harus sepanjang 10 digits!')
    
    else :
        # Jika NPM tidak berbentuk angka
        print('NPM harus berupa angka!')

# Input mulai interogasi jika N
elif x == 'N' :
    print ('Tidak jadi interogasi')

# Input mulai interogasi jika tidak Y/N
else :
    print ('Input tidak valid!')
    x = input('Mulai Interogasi (Y/N)? ')
    if x == 'Y':
        print('Mari kita mulai interogasi')
        a = input ('Siapa namamu? ')
        b = input ('Berapa nomor NPM mu? ')
        # NPM digit
        while b :
            k = b.isdigit()
            l = list(b)
            if k == True:
                count = 0
                for i in l:
                    count = count+1
                    
                if count == 10: 
                    
                    c = input ('Apakah kamu punya motif (Y/N)? ')
                    # motif
                    if c == 'Y':
                        d = input('Apa motif kamu tadi? ')
                        e = input('Apakah kamu punya alibi (Y/N)? ')
                        # Alibi
                        if e == 'Y':
                            f = input('Apa alibi kamu? ')
                            print(f'''{a} dengan NPM {b} memiliki motif {d} dan memiliki alibi {f} 
                            {a} lumayan mencurigakan nih... ''')
                            # Lanjut Interogasi
                            print('----------------------------------------')
                                    
            
                        elif e == 'N':
                            print(f'''{a} dengan NPM {b} memiliki motif {d} tapi tidak memiliki alibi
                            Wah, {a} mencurigakan nihh >:( ''')
                            print('----------------------------------------')
                                    

                    elif c == 'N':
                        e = input('Apakah kamu punya alibi (Y/N)? ')
                        if e == 'Y':
                            f = input('Apa alibi kamu? ')
                            print(f'''{a} dengan NPM {b} tidak memiliki motif dan memiliki alibi {f}
                            {a} tidak terlalu mencurigakan sih''')
                            print('----------------------------------------')
                            
                        elif e == 'N':
                            print(f'''{a} dengan NPM {b} tidak memiliki motif maupun alibi 
                            {a} lumayan mencurigakan nih...''')
                            print('----------------------------------------')

                            y = input ('Lanjut interogasi (Y/N)? ')
                            if y == 'N':
                                print ('Interogasi telah selesai')
                            else :
                                print ('Input tidak valid')

                            break

                        else :
                            print('Seseorang harus punya alibi atau tidak punya alibi sama sekali!')
                            print('----------------------------------------')

                            
                    else :
                        print('Seseorang harus punya motif atau tidak punya motif sama sekali!')
                        print('----------------------------------------')

                else:
                    for b in range (1) :
                        print('NPM harus sepanjang 10 digits!')
                        print('----------------------------------------')
                                        
            
            else :
                for b in range (1) :
                    print('NPM harus berupa angka!')
                    print('----------------------------------------')
                
            a = input ('Siapa namamu? ')
            b = input ('Berapa nomor NPM mu? ')
            

print('''>>==========================<<
||                     	    ||
|| Ending the Interrogation ||
||                     	    ||
>>==========================<<'''
)
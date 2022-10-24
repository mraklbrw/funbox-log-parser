

def main():
    with open('events.log') as f:
        nok_count = 0
        date_ = ''

        for line in f:
            line = line.rstrip()
            tmp_line = line.split(':')
            
            if tmp_line[2].split(' ')[1] == 'OK':
                continue

            cur_date = tmp_line[0] + ':' + tmp_line[1] # [2018-04-13 06:26

            if cur_date != date_:
                if date_ != '':
                    print(f'{date_}: {nok_count}')
                date_ = cur_date
                nok_count = 1
            else:
                nok_count += 1
            
        print(f'{date_}: {nok_count}')
                

if __name__ == '__main__':
    main()


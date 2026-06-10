import pickle
import os
import re


FILE_PATH = "members.pickle"


# FN-001 데이터 로드
def load_data(path):
    # 프로그램 시작 시 1회 실행
    # path에 해당하는 바이너리 파일을 pickle.load로 읽음
    
    
    # 파일이 없거나 손상되면 빈 딕셔너리 반환
    

    #pickle 파일 여기서 오픈하게 만듬
    try:
        with open(path, "rb") as file:
            members = pickle.load(file)
            return members

    except FileNotFoundError:
        return []

    except EOFError:
        return []

    except pickle.UnpicklingError:
        return []


# FN-002 메뉴 출력
def print_menu():

    print("1. 회원 추가")
    print("2. 회원 목록 보기")
    print("3. 회원 정보 수정하기")
    print("4. 회원 삭제")
    print("5. 종료")



def print_menu():
    # 메뉴 출력 후 사용자 입력값을 문자열로 반환

    print("==============================")
    print("다음 메뉴 중 하나를 선택하세요.")
    print("==============================")
    print("1. 회원 추가")
    print("2. 회원 목록 보기")
    print("3. 회원 정보 수정하기")
    print("4. 회원 삭제")
    print("5. 종료")

    choice = input("메뉴 선택: ")

    return choice


# FN-003 회원 추가
#dictionary set
def add_member(members):
    print("회원 정보를 입력하세요.")

    while True:
        name = input("이름: ")

        if not validate_name(name):
            continue

        break

    while True:
        phoneNum = input("전화번호: ")

        if not validate_phone(phoneNum):
            continue

        break

    address = input("주소: ")

    while True:
        member_type = input("종류: ")

        if not validate_type(member_type):
            continue

        break

    members.append(
        {
            "name": name,
            "phoneNum": phoneNum,
            "address": address,
            "category": member_type
        }
    )

    print("회원 정보가 등록되었습니다.")

    

# FN-004 회원 목록 조회

# 총 3 명의 회원이 저장되어 있습니다.
# 회원정보 : 이름 = 윤아, 전화번호 : 01012345678, 주소 : 서울시, 종류 : 친구

def list_members(members):

    #f-string으로 출력
    print(f"총 {len(members)}명의 회원이 저장되었습니다.")

    for member in members:
        print(f"회원정보: 이름 = {member["name"]}, 전화번호: {member["phoneNum"]}, 주소: {member["address"]}, 구분: {member["type"]}")



# FN-005 이름으로 회원 검색
# 여기에다 검색을 맡기는 코드
def find_by_name(members, name) -> list:
    # 전체 회원을 순회하면서 이름이 일치하는 회원을 리스트로 수집
    # 동명이인 처리를 위해 list로 반환
    result = []

    for member in members:
        if member["name"] == name:
            result.append(member)

        return result
    


# FN-006 회원 정보 수정
def update_member(members):
    # 수정할 이름 입력
    name = input("수정할 이름을 입력하세요")
    # find_by_name()으로 검색
    result = find_by_name(members, name)
    # 0건이면 안내 후 복귀
    if len(result) == 0:
        print("해당 회원이 없습니다.")
        return
    # 1건이면 그 검색될 한명으로 수정 대상 확정
    if len(result) == 1:
        index = 0
    #2건 이상이면
    else: 
        for i, member in enumerate(result, start =1)
            print(f"{i}. member['name'] / {member['phoneNum']} / {member['address']} / {member['type']}")
    
        num = int(input("수정할 번호를 선택하세요: "))

        if num < 1 or num > len(result):
            print("잘못된 번호입니다.")
            return

        index = num - 1

    
# FN-007 회원 삭제
def delete_member(members):
    # 삭제할 이름 입력
    print("삭제할 회원의 이름을 입력하세요.")
    name = input("이름 : ")
    
    
    # find_by_name()으로 검색
    result = find_by_name(members, name)
    
    # 0건이면 안내 후 복귀
    if len(result) == 0:
        print("해당하는 회원 정보가 없습니다.")
    # 1건이면 바로 삭제
    elif len(result) == 1:
        target = result[0]
        members.remove(target)
        print("삭제가 완료됬습니다. ")
    # 2건 이상이면 번호 선택 후 삭제
    else:
        print(f"총 {len(result)}개의 목록이 검색되었습니다.")
        print("아래 목록 중 삭제할 회원의 번호를 입력하세요.")
    
    #for문과 enumerate로 리스트에서 같은 이름들 찾기    
    # 삭제 완료 메시지 출력
        for i, member in enumerate(result, start = 1):
            print(
                f"{i}. 이름 = {member["name"]},"
                f"전화번호 : {member["phoneNum"]}"
                f"주소: {member["address"]},"
                f"구분: {member["type"]}" 
            )

        num = int(input())

        if num < 1 or num > len(result):
            print("잘못된 번호입니다.")
            return
        
        removedResult = result[num - 1]
        members.remove(removedResult)

        print("삭제가 완료되었습니다.")



# FN-009 이름 유효성 검사
def validate_name(name):
    # 이름은 1~5자만 허용
    if len(name) < 1 or len(name) > 5:
        print("이름은 1자 이상 5자 이하로 입력하세요.")
        return False

    return True



# FN-009 전화번호 유효성 검사
def validate_phone():
    # 전화번호 형식 검사
    # 정규식 권장: ^010\d{8}$
    while True:
        phoneNum = input("전화번호: ")

    #validatenumber
        if not re.fullmatch(r"010\d{8}$", phoneNum):
            print("전화 번호는 010 뒤 8자리 숫자여야합니다.")
            continue
        
        return phoneNum


# FN-009 회원 종류 유효성 검사
def validate_type(member_type):
    # 가족 / 친구 / 기타 중 하나인지 검사
     if member_type not in ["가족", "친구", "기타"]:
        print("회원 종류는 가족, 친구, 기타 중 하나만 입력하세요.")
        return False

     return True


# FN-008 데이터 저장
def save_data(path, members):
    # 종료 메뉴 5 선택 시 실행
    # members 딕셔너리를 pickle.dump로 바이너리 파일에 저장

    with open(path, "wb") as file:
        pickle.dump(members, file)

# FN-010 예외 처리
# 파일 예외는 load_data()에서 처리
# 메뉴 입력 예외는 main() 루프에서 처리
# 검색 결과 0건은 update_member(), delete_member()에서 처리
# 유효성 실패는 add_member(), update_member() 안에서 재입력 루프로 처리


def main():
    # 프로그램 시작
    DB_FILE = "members.pickle"
    member_db = load_data(DB_FILE)

    while True:
        choice = print_menu()

        if choice == "1":
            add_member(member_db)

        elif choice == "2":
            list_members(member_db)

        elif choice == "3":
            update_member(member_db)

        elif choice == "4":
            delete_member(member_db)

        elif choice == "5":
            save_data(FILE_PATH, member_db)
            print("종료되었습니다.")
            break

        else:
            print("잘못된 입력입니다.")




#main()으로 마지막에 실행 
if __name__ == "__main__":
    main()
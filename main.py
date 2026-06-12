import pickle
import os
import re
DB_FILE = "members.pickle"  #피클파일

def load_data():
    # 프로그램 시작 시 1회 실행
    # pickle 파일 여기서 오픈하게 만듬  없으면 그냥 리스트 반환
    try:
        with open(DB_FILE, "rb") as file:
            members = pickle.load(file)
            return members
    except FileNotFoundError:
        return []
    except EOFError:
        return []

#validate (유효성 검사) 은 전부 True/ false 로 반환하는 검사함수로 만듬. 
def validate_name(name):
    # 이름은 1~5자만 허용
    if len(name) < 1 or len(name) > 5:
        print("이름은 1자 이상 5자 이하로 입력하세요.")
        return False

    return True


# FN-009 전화번호 유효성 검사
def validate_phone(phoneNum):
    # 전화번호 형식 검사
    # 정규식 권장: ^010\d{8}$
    if not re.fullmatch(r"010\d{8}", phoneNum):
        print("전화번호는 010 뒤 8자리여야 됩니다.")
        return False
    
    return True


# FN-009 회원 구분 유효성 검사
def validate_member(member_type):
    # 가족 / 친구 / 기타 중 하나인지 검사
    if member_type  not in ["가족", "친구", "기타"]:
        print("회원 구분는 가족, 친구, 기타 중 하나만 입력하세요.")
        return False

    return True

# FN-003 회원 추가
# dictionary set
#add_member() 에서 인풋을 받을거임
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
        member_type = input("구분: ")

        if not validate_member(member_type):
            continue
        break

    members.append(
        {
            "name": name,
            "phoneNum": phoneNum,
            "address": address,
            "member_type": member_type,
        }
    )
    print("회원 정보가 등록되었습니다.")


def list_members(members):

    print(f"총 {len(members)}명의 회원이 저장되었습니다.")

    for member in members:
        print(
            f"회원정보: 이름 = {member['name']}, "
            f"전화번호: {member['phoneNum']}, "
            f"주소: {member['address']}, "
            f"구분: {member['member_type']}"
        )

# 검색을 맡기는 코드 / 동명이인 처리를 위해 list 로 반환
def find_by_name(members, name):
  
    result = []

    for member in members:
        if member["name"] == name:
            result.append(member)

    return result


# FN-006 회원 정보 수정
def update_member(members):
  
    name = input("수정할 이름을 입력하세요: ")
    # find_by_name()으로 검색
    result = find_by_name(members, name)
    # 0건이면 안내 후 복귀
    if len(result) == 0:
        print("해당 회원이 없습니다.")
        return
    # 1건이면 그 검색될 한명으로 수정 대상 확정
    if len(result) == 1:
        target = result[0]
    # 2건 이상이면
    else:
        print(f"총 {len(result)}개의 목록이 검색되었습니다.")
        print("아래 목록 중 수정할 회원의 번호를 입력하세요.")
        
        for i, member in enumerate(result, start=1):
            print(
                f"{i}. 이름 = {member['name']},"
                f"전화번호 : {member['phoneNum']}"
                f"주소 : {member["address"]}"
                f"구분 : {member["member_type"]}"
            )

        num = int(input("수정할 번호를 선택하세요: "))

        if num < 1 or num > len(result):
            print("잘못된 번호입니다.")
            return

        target = result[num - 1]
        
    print("수정할 정보를 입력하세요.")
        
    while True:
        new_name = input("새 이름: ")
        if validate_name(new_name):
            break
    
    while True:
        new_phone = input("새 전화번호:")
        if validate_phone(new_phone):
            break
    
    new_address = input("새로운 주소: ")
    
    while True:
        new_type = input("새 종류: ")
        if validate_member(new_type):
            break
      
    target["name"] = new_name
    target["phoneNum"] = new_phone
    target["address"] = new_address
    target["member_type"] = new_type
    
    print("수정이 완료되었습니다.")
    

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

        # for문과 enumerate로 리스트에서 같은 이름들 찾기
        # 삭제 완료 메시지 출력
        for i, member in enumerate(result, start=1):
            print(
                f"{i}. 이름 = {member['name']}, "
                f"전화번호 = {member['phoneNum']}, "
                f"주소 = {member['address']}, "
                f"구분 = {member['member_type']}"
            )

        num = int(input())

        if num < 1 or num > len(result):
            print("잘못된 번호입니다.")
            return

        removedResult = result[num - 1]
        members.remove(removedResult)

        print("삭제가 완료되었습니다.")



# FN-008 데이터 저장
def save_data(members):
    # 종료 메뉴 5 선택 시 실행
    # members 딕셔너리를 pickle.dump로 바이너리 파일에 저장

    with open(DB_FILE, "wb") as file:
        pickle.dump(members, file)


def main():
    member_db = load_data()

    while True:
        print("다음메뉴중 하나")
        print("1. 회원 추가")
        print("2. 회원 목록 보기")
        print("3. 회원 정보 수정하기")
        print("4. 회원 삭제")
        print("5. 종료")
        choice = input("메뉴 선택: ")

        if choice == "1":
            add_member(member_db)
            
        elif choice == "2":
            list_members(member_db)
        elif choice == "3":
            update_member(member_db)
        elif choice == "4":
            delete_member(member_db)
        elif choice == "5":
            save_data(member_db)
            print("종료되었습니다.")
            break

        else:
            print("잘못된 입력입니다.")

# main()으로 메뉴 출력
if __name__ == "__main__":
    main()
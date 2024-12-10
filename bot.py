import pywikibot

def fetch_category_members(category_name, site):
    # 목록 문서 가져오기
    category = pywikibot.Category(site, category_name)
    members = category.articles(namespaces=0)  # 주로 문서(namespace 0)만 가져옴
    return members

def update_page_with_list(page_title, members, site):
    # 갱신
    page = pywikibot.Page(site, page_title)
    # 새로운 목록 생성
    new_content = "== 삭제 제안 문서 목록 ==\n\n"
    new_content += "\n".join([f"* [[{member.title()}]]" for member in members])
    new_content += "\n\n이 목록은 자동으로 업데이트됩니다."

    # 페이지 업데이트
    try:
        page.text = new_content
        page.save(summary="자동화: 삭제 제안 문서 목록 갱신")
        print(f"페이지 '{page_title}'가 성공적으로 업데이트되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    site = pywikibot.Site("ko", "wikipedia")

    category_name = "분류:삭제 제안 문서"
    page_title = "위키백과:삭제 토론/삭제 제안/리스트"

    # 문서 목록 가져오기 및 업데이트
    members = fetch_category_members(category_name, site)
    update_page_with_list(page_title, members, site)

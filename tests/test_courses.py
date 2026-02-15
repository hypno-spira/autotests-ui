import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверить наличие и текст заголовка "Courses"
    courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses).to_be_visible()
    expect(courses).to_have_text('Courses')

    # Проверить наличие и текст блока "There is no results"
    no_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results).to_be_visible()
    expect(no_results).to_have_text('There is no results')

    # Проверить наличие и видимость иконки пустого блока
    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(text).to_be_visible()
    expect(text).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    # 1. Открыть страницу
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # 2. Проверить наличие заголовка "Create course"
    create_course_page.check_visible_create_course_title()

    # 3. Проверить, что кнопка создания курса недоступна для нажатия
    create_course_page.check_disabled_create_course_button()

    # 4. Убедиться, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()

    # 5. Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)

    # 6. Проверить, что форма создания курса отображается и содержит значения по умолчанию.
    create_course_page.check_visible_create_course_form(title="", estimated_time="", description="", max_score="0",
                                                        min_score="0")

    # 7. Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()

    # 8. Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()

    # 9. Убедиться, что отображается блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # 10. Загрузить изображение для превью курса
    create_course_page.upload_preview_image(file="./testdata/files/image.png")

    # 11. Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.check_visible_image_upload_view()

    # 12. Заполнить форму создания курса значениями
    create_course_page.fill_create_course_form(title="Playwright", estimated_time="2 weeks", description="Playwright",
                                               max_score="100", min_score="10")

    # 13. Нажать на кнопку создания курса
    create_course_page.click_create_course_button()

    # 14. После создания курса произойдет редирект на страницу со списком курсов. Необходимо проверить наличие заголовка "Courses"
    courses_list_page.check_visible_courses_title()

    # 15. Проверить наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()

    # 16. Проверить корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(index=0, title="Playwright", max_score="100", min_score="10",
                                                estimated_time="2 weeks")

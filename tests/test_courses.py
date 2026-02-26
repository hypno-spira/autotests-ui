import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


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
    # 5. Проверить, что блок загрузки изображения отображается в состоянии, когда картинка не выбрана
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)


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
    create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")

    # 11. Убедиться, что блок загрузки изображения отображает состояние, когда картинка успешно загружена
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # 12. Заполнить форму создания курса значениями
    create_course_page.fill_create_course_form(title="Playwright", estimated_time="2 weeks", description="Playwright",
                                               max_score="100", min_score="10")

    # 13. Нажать на кнопку создания курса
    create_course_page.click_create_course_button()

    # 14. После создания курса произойдет редирект на страницу со списком курсов. Необходимо проверить наличие заголовка "Courses"
    # 15. Проверить наличие кнопки создания курса
    courses_list_page.toolbar_view.check_visible()

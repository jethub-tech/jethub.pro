import streamlit as st
from PIL import Image


def main() -> None:
    st.set_page_config(
        page_title="JetHub.pro",
        page_icon="https://github.com/jethub-tech/jethub.pro/blob/master/images/logo.png",
        layout="wide",
        initial_sidebar_state="auto",
        # menu_items={
        #     "Get Help": "https://www.extremelycoolapp.com/help",
        #     "Report a bug": "https://www.extremelycoolapp.com/bug",
        #     "About": "# This is a header. This is an *extremely* cool app!",
        # }
    )

    st.image(
        Image.open("./static/logo-invert.png"),
        width=180,
        clamp=True,
    )

    st.title("JetHub")
    st.subheader("Делаем ML инструменты для повышения эффективности процесса DevSecOps")

    st.markdown("----")
    col_for_1, col_for_2, col_for_3 = st.columns(
        spec=3,
        gap="small",
    )

    with col_for_1:
        st.write(
            """
            ## Для разработчиков
            Ранжируем SAST отчеты по вероятности ложно-положительных (false positivie) ошибок
            """
        )

    with col_for_2:
        st.write(
            """
            ## Для безопасников
            Предлагаем исправления уязвимостей в коде (в процессе)
            """
        )

    with col_for_3:
        st.write(
            """
            ## Для руководителей
            Обогащаем результаты ошибок дополнительной информацией ошибок (в процессе)
            """
        )

    st.markdown("----")
    st.write("## Пример прототипа")
    st.image(
        Image.open("./static/example_mvp.png"),
        use_column_width="auto",
        clamp=True,
    )

    st.markdown("----")
    col_feedback_1, col_feedback_2 = st.columns(
        spec=2,
        gap="large",
    )

    with col_feedback_1:
        st.write("# [Написать письмо](mailto:babenkormn@gmail.com)")

    with col_feedback_2:
        st.write("# [Написать в telegram](https://t.me/bblazee)")


if __name__ == "__main__":
    main()

# final_project_of_autotesting
Final project of stepik course "Autotesting with Selenium and Python". Module 4.

Use this command for full file

            'pytest -v -s --tb=line --language=en test_main_page.py'

Use this command for a special test case

            'pytest -v -s --tb=line --language=en test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page'

Use this command when you are using marks

            'pytest -v -s --tb=line --language=en -m login_guest'
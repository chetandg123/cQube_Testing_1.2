import time
import unittest
from SI.MAP.Click_on_School_infra import click_schoolinfra
from SI.MAP.check_districtwise_school import districtlevel_school
from SI.MAP.check_infrascore_with_download_functionality import SchoolInfra_scores
from SI.MAP.check_sc_map_blockwise_records import school_map_blockwise
from SI.MAP.check_sc_map_clusterwise_records import test_school_map_schoollevel_records

from SI.MAP.check_sc_map_districtwise_records import sc_map_districtwise
from SI.MAP.check_with_districts_from_select_box import District_names
from SI.MAP.check_with_map_on_schoolinfra import check_markers_on_map
from SI.MAP.check_with_schoolinfra_options import School_infra_options
from SI.MAP.click_on_Dashboard import click_dashboard

from SI.MAP.click_on_Report_from_scinfra import click_report
from SI.MAP.click_on_Reportmap import click_on_reportmap
from SI.MAP.click_on_anydistrict_and_download_csv import download_icon
from SI.MAP.click_on_blk_clus_school_and_home import click_on_home
from SI.MAP.click_on_block_and_home import block_level_home

from SI.MAP.click_on_block_check_with_footer_values import school_count
from SI.MAP.click_on_block_cluster_school_and_check_schoolscount import Block_school_count
from SI.MAP.click_on_blocks import click_on_blocks
from SI.MAP.click_on_blocks_and_scores import block_btn_scores
from SI.MAP.click_on_blocksbtn_and_check_download import Blockwise_csv_download

from SI.MAP.click_on_blockwise_download_csv import cluster_level_map_check
from SI.MAP.click_on_cluster_and_home import click_cluster_and_home
from SI.MAP.click_on_cluster_check_download import clusterwise_download
from SI.MAP.click_on_clusters import cluster_button
from SI.MAP.click_on_clusters_and_scores import cluster_btn_scores

from SI.MAP.click_on_district_and_homeicon import district_home
from SI.MAP.click_on_district_options import District_options
from SI.MAP.click_on_hyperlink import click_on_hyperlink
from SI.MAP.click_on_infra_score import click_on_infrascores
from SI.MAP.click_on_infra_scores_options import select_infrascore_options

from SI.MAP.click_on_school_and_check_download import school_wise_download
from SI.MAP.click_on_school_infrastructure import School_infra_test
from SI.MAP.click_on_schools import click_schoolwise
from SI.MAP.click_on_schools_and_scores import schools_btn_scores
from SI.MAP.download_clusterlevel_csv import cluster_level_csv

from SI.MAP.download_districtwise_csv import districtwise_csv
from SI.MAP.mouseover_on_districtwise import mouseover
from SI.MAP.select_district_block_from_select_box import select_blockwise

from reuse_func import GetData


class cQube_SI_Map_Report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        time.sleep(5)

    def test_check_district_names(self):
        b = District_names(self.driver)
        result = b.test_districtlist()
        self.assertNotEqual(0, result, msg="All Districts are not present in select box!..")
        print("District names order checked")

    def test_check_markes_on_map(self):
        b = check_markers_on_map(self.driver)
        result = b.test_map()
        self.assertNotEqual(0, result, msg="Data not present on map")
        self.data.page_loading(self.driver)
        print("markers on map ")

    def test_infrascore(self):
        b = SchoolInfra_scores(self.driver)
        infra_score = b.infra_score()
        b.remove_csv()
        self.assertNotEqual(0, infra_score, msg='Failed')

        boy_toilet = b.Boys_toilet_percentage()
        b.remove_csv()
        self.assertNotEqual(0, boy_toilet, msg='Failed')

        drinking_water = b.drinking_water()
        b.remove_csv()
        self.assertNotEqual(0, drinking_water, msg='Failed')

        Electricity = b.Electricity()
        b.remove_csv()
        self.assertNotEqual(0, Electricity, msg='Failed')

        girl_toilet = b.girls_toilet()
        b.remove_csv()
        self.assertNotEqual(0, girl_toilet, msg='Failed')

        Handpump = b.Handpump()
        b.remove_csv()
        self.assertNotEqual(0, Handpump, msg='Failed')

        Handwash = b.Handwash()
        b.remove_csv()
        self.assertNotEqual(0, Handwash, msg='Failed')

        Library = b.Library()
        b.remove_csv()
        self.assertNotEqual(0, Library, msg='Failed')

        Solar_panel = b.Solar_panel()
        b.remove_csv()
        self.assertNotEqual(0, Solar_panel, msg='Failed')

        Tapwater = b.Tapwater()
        b.remove_csv()
        self.assertNotEqual(0, Tapwater, msg='Failed')

        Toilet = b.Toilet()
        b.remove_csv()
        self.assertNotEqual(0, Toilet, msg='Failed')

    def test_school_infra_options(self):
        b = School_infra_options(self.driver)
        res1, res2 = b.test_options()
        self.assertEqual(res1, "Report", msg="option is not available")
        self.assertEqual(res2, "Map based Report", msg="option is not available")
        print("School infrastructure report contains two reports ")
        self.data.page_loading(self.driver)

    def test_download(self):
        b = download_icon(self.driver)
        res = b.test_donwload()
        if "school-infra-map" in self.driver.current_url:
            print("School infrastructure map based report present")
        else:
            print("School infra map report is not exist")

    def test_click_on_home(self):
        b = click_on_home(self.driver)
        c1, c2, c3 = b.test_home()
        self.assertNotEqual(0, c1, msg="Records are not present on map ")
        self.assertNotEqual(0, c2, msg="Records are not present on map ")
        self.assertNotEqual(0, c3, msg="Records are not present on map ")
        print("cluser level home icon is working")

    def test_blockelevel_home_click(self):
        b = block_level_home(self.driver)
        res = b.test_blocks()
        if "school-infra-map" in self.driver.current_url:
            print("School infra map based report")
        else:
            print("school infra map report is not loaded ")

    def test_school_count(self):
        b = school_count(self.driver)
        res = b.test_count()
        self.assertNotEqual(0, int(res), msg="wrong schools count")
        print("checked with school count values")


    def test_no_of_schools(self):
        b = Block_school_count(self.driver)
        r, r1, r2, r3 = b.test_counter()
        self.assertEqual(int(r), int(r1), msg="mis match found in no of school in block level")
        self.assertEqual(int(r), int(r2), msg="mis match found in no of school in cluster level")
        self.assertEqual(int(r), int(r3), msg="mis match found in no of school in school level")
        self.data.page_loading(self.driver)
        print("checked with comapared with footer values ")

    def test_click_on_block(self):
        b = click_on_blocks(self.driver)
        res = b.test_blocks_button()
        self.assertNotEqual(0, res, msg="Records are not present on map ")
        print("Block buttons is working...")

    def test_blocklevel_file(self):
        b = Blockwise_csv_download(self.driver)
        result = b.test_download_blockwise()
        self.assertNotEqual(0, result, msg="Records are not present on map ")
        print("blocklevel file is downloaded")

    def test_clusterlevel_map(self):
        b = cluster_level_map_check(self.driver)
        result = b.test_blockwise_data()
        self.assertNotEqual(0, result, msg="markers are not present on map ")
        print("clusterlevel map is loaded")

    def test_cluster_and_homebtn(self):
        b = click_cluster_and_home(self.driver)
        res = b.test_cluster()
        self.assertNotEqual(0, res, msg="cluster level markers not present on map ")
        print("cluster level home icon is working ")

    def test_clusterwise_download(self):
        b = clusterwise_download(self.driver)
        result = b.test_download()
        self.assertNotEqual(0, result, msg="Records are not present on map ")
        print("cluster wise csv is downloading working")

    def test_clusterbtn(self):
        b = cluster_button(self.driver)
        self.assertNotEqual(0, b, msg="Records are not present on map ")
        print("cluster button is working ")

    def test_dashboard(self):
        b = click_dashboard(self.driver)
        res = b.test_dashboard()
        self.assertEqual("cQube - Dashboard", res, msg="Dashboard is not exists!")
        print("checked with dashboard ")
        self.data.page_loading(self.driver)

    def test_click_home_in_districtwise(self):
        b = district_home(self.driver)
        res = b.test_district()
        if "school-infra-map" in self.driver.current_url:
            print("school infra map based report present")
        else:
            print("home icon is not working ")

    def test_district_options(self):
        b = District_options(self.driver)
        res = b.test_options()
        self.assertNotEqual(0, res, msg="district list are present")
        print("checked with districtwise select box")

    def test_hyperlink(self):
        b = click_on_hyperlink(self.driver)
        res = b.test_link()
        if "school-infra-map" in self.driver.current_url:
            print("school infra map based report present")
        else:
            print("home icon is not working ")

    def test_infrascores(self):
        b = click_on_infrascores(self.driver)
        res = b.test_infrascores()
        self.assertNotEqual(0, res, msg="infra score options not contains in drop down")
        print("checked with infrascores options")

    def test_report(self):
        b = click_report(self.driver)
        self.data.page_loading(self.driver)
        res = b.test_infra()
        if "school-infrastructure" in self.driver.current_url:
            print("Shool infrastructure report page")
        else:
            print("School infrastructure report page is not exist")
        self.data.page_loading(self.driver)

    def test_reportmap(self):
        b = click_on_reportmap(self.driver)
        self.data.page_loading(self.driver)
        res = b.test_reportmap()
        self.assertEqual("cQube - Dashboard", res, msg="Dashboard is not exists!")
        self.data.page_loading(self.driver)
        print("report map is present on dashboard")

    def test_schoolwise_download(self):
        b = school_wise_download(self.driver)
        res = b.test_schoolwise()
        time.sleep(3)
        self.assertNotEqual(0, res, msg="Records are not present on map ")
        print("school wise csv is downloaded")

    def test_click_on_school(self):
        b = click_schoolinfra(self.driver)
        res = b.test_schoolinfra()
        if "school-infrastructure" in self.driver.current_url:
            print("School-infrastructure page")
        else:
            print("Not school-infrastructure page")

    def test_click_schoolwise(self):
        b = click_schoolwise(self.driver)
        self.assertNotEqual(0, b, msg="Records are not present on map ")
        print("school button is working ")

    def test_dashboard_option(self):
        b = School_infra_test(self.driver)
        res = b.test_dashboard_option()
        if "school-infra-map" in self.driver.current_url:
            print("School infra map based report page exist")
        else:
            print("School infra map based report page not exist")
        self.data.page_loading(self.driver)

    def test_infrascore_click(self):
        b = select_infrascore_options(self.driver)
        res = b.test_infrascores()
        self.assertNotEqual(0, res, msg="infra score options not contains in drop down")
        print("infra scores options are working ")

    def test_clusterwise_csv(self):
        b = cluster_level_csv(self.driver)
        res = b.test_clusterwise()
        print("Clustwise csv file is downloaded...")

    def test_districtwise_csv(self):
        b = districtwise_csv(self.driver)
        res = b.test_districtwise()
        print("Districtwise csv file is downloaded...")

    def test_mouseover_on_dots(self):
        b = mouseover(self.driver)
        res = b.test_mousehover()
        count = self.data.test_mouse_over()
        self.assertNotEqual(0, count, msg="markers not present in map ")
        print("markers present on map ")

    def test_blockwise(self):
        b = select_blockwise(self.driver)
        res = b.test_dist_blocks()
        print("checked blockwise data ")

    def test_block_scores(self):
        b = block_btn_scores(self.driver)
        result = b.test_click_blocks()
        self.data.page_loading(self.driver)
        print("block button is worked and infra scores is working ")

    def test_clusters_scores(self):
        b = cluster_btn_scores(self.driver)
        result = b.test_click_clusters()
        self.data.page_loading(self.driver)
        print("cluster button is worked and infra scores is working ")

    def test_schools_scores(self):
        b = schools_btn_scores(self.driver)
        res = b.test_click_schools()
        self.data.page_loading(self.driver)
        print("school button is worked and infra scores is working ")

    def test_districtwise_school(self):
        b = districtlevel_school(self.driver)
        result = b.test_districtwise_schoolscount()
        self.assertNotEqual(0, result, msg="markers are not present on map ")
        self.data.page_loading(self.driver)
        print("District wise records validated")

    def test_sc_map_districtwise(self):
        b = sc_map_districtwise(self.driver)
        result = b.test_schools()
        print("district wise map records checked")

    def test_sc_map_blockwise(self):
        b = school_map_blockwise(self.driver)
        result = b.test_schools()
        self.assertEqual(0,result,msg="No data found")
        print("blockwise wise map records checked")


    def test_schools_per_cluster_csv_download1(self):
        self.driver = self.data.get_driver_SIMAP_Download1()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        school = test_school_map_schoollevel_records(self.driver)
        result = school.check_download_csv1()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download1 is working")


    def test_schools_per_cluster_csv_download2(self):
        self.driver = self.data.get_driver_SIMAP_Download2()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        school = test_school_map_schoollevel_records(self.driver)
        result = school.check_download_csv2()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download2 is working")


    def test_schools_per_cluster_csv_download3(self):
        self.driver = self.data.get_driver_SIMAP_Download3()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        school = test_school_map_schoollevel_records(self.driver)
        result = school.check_download_csv3()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download3 is working")


    def test_schools_per_cluster_csv_download4(self):
        self.driver = self.data.get_driver_SIMAP_Download4()
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.navigate_to_school_infrastructure_map()
        school = test_school_map_schoollevel_records(self.driver)
        result = school.check_download_csv4()
        if result == 0:
            print("Schools per cluster csv download report is working")
            print("on selection of each district,block and cluster")
            print("The footer value of no of schools and no of students are")
            print("equals to downloaded file")
        else:
            raise self.failureException("Schools per cluster csv report download4 is working")






    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


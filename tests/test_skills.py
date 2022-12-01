from . import ClientTestCase
from client.models import Skill, SkillsResponse


class TestSkills(ClientTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.skills_data = self.client.GetSkills()
        self.mock_skills_data = self.get_mock_skills_data()

    def test_skills_api_success(self):
        self.assertEqual(self.skills_data.headers.response_code, '0000')

    def test_skills_api_return_type_data(self):
        self.assertIsInstance(self.skills_data, SkillsResponse)

    def test_skills_api_return_type_list(self):
        self.assertIsInstance(self.skills_data.body, list)

    def test_skills_api_return_type_single(self):
        self.assertIsInstance(self.skills_data.body[0], Skill)

    def test_skills_with_data(self):
        self.assertIsInstance(self.mock_skills_data, SkillsResponse)
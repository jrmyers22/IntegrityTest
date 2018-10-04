from DataCollection import ProjectStructureTree
import unittest


class TestProjectStructureTree(unittest.TestCase):

    def test_project_structure_tree(self):
        test_project = "TestProject"
        class_names = ['these', 'are', 'the', 'seperate', 'class', 'names', 'for', 'the', 'project']
        method_names = ['these', 'are', 'the', 'seperate', 'method', 'names', 'for', 'the', 'classes']
        structures_list = ['for', 'if', 'while', 'elif', 'elif', 'elif']
        project = ProjectStructureTree.ProjectNode(test_project, class_names)
        for j in range(project.class_numbers):
            for i in range(len(method_names)):
                project.class_list[j].add_method_node(method_names[i])

        for i in range(project.class_numbers):
            for j in range(len(method_names)):
                for k in range(len(structures_list)):
                    project.class_list[i].method_node_list[k].add_structure_node(structures_list[k])

        for j in range(project.class_numbers):
            self.assertEqual(project.class_list[j].class_name, class_names[j])

        for i in range(project.class_numbers):
            for j in range(len(method_names)):
                for k in range(len(structures_list)):
                    self.assertEqual(project.class_list[i].method_node_list[k].method_name, method_names[k])


if __name__ == '__main__':
    unittest.main()
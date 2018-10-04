
class ProjectNode:
    def __init__(self, project_name, class_names):
        self.project_name = project_name
        self.class_list = []
        self.class_numbers = 0
        for i in range(len(class_names)):
            self.class_list.append(ClassTreeNode(class_names[i], self))
            self.class_numbers = self.class_numbers + 1;

    def add_class_node(self, class_name, method_names=None, structures_list=None):
        self.class_list.append(ClassTreeNode(class_name, self, method_names, structures_list))


class ClassTreeNode:

    def __init__(self, class_name, project_node, method_names=None, structures_list=None, dependencies_list=None):
        self.class_name = class_name
        self.project_node = project_node
        self.method_node_list = []
        self.dependencies_list = dependencies_list
        if method_names is not None:
            for i in range(len(method_names)):
                self.method_node_list.append(MethodTreeNode(method_names[i], self, structures_list))

    def add_method_node(self, method_names, structures_list=None):
        if self.method_node_list is None:
            self.method_node_list = []
            self.method_node_list.append(MethodTreeNode(method_names, self))
        else:
            self.method_node_list.append(MethodTreeNode(method_names, self))

    def add_dependency(self, dependency_name, project_node, method_names, structures_list):
        if self.dependencies_list is None:
            self.dependencies_list = []
            self.dependencies_list.append(ClassTreeNode(dependency_name, project_node, method_names, structures_list))
        else:
            self.dependencies_list.append(ClassTreeNode(dependency_name, project_node, method_names, structures_list))


class MethodTreeNode:

    def __init__(self, method_name, class_node, structures_list=None):
        self.method_name = method_name
        self.class_node = class_node
        self.structures_nodes = []
        if structures_list is not None:
            for i in range(len(structures_list)):
                self.structures_nodes.append(StructureTreeNode(structures_list[i], self))

    def add_structure_node(self, structure_name):
        if self.structures_nodes is None:
            self.structures_nodes = []
            self.structures_nodes.append(StructureTreeNode(structure_name, self))
        else:
            self.structures_nodes.append(StructureTreeNode(structure_name, self))


class StructureTreeNode:

    def __init__(self, structure_name, method_node, inner_structures=None):
        self.structure_name = structure_name
        self.method_node = method_node
        self.inner_structures = inner_structures

    def add_inner_structure(self, inner_structure_name):
        if self.inner_structures is None:
            self.inner_structures = []
            self.inner_structures.append(StructureTreeNode(inner_structure_name, self.method_node))
        else:
            self.inner_structures.append(StructureTreeNode(inner_structure_name, self.method_node))


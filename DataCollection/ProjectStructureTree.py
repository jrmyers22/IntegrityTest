# Overall project node, can have multiple for a whole class and compare them to check equality
class ProjectNode:
    # Constructor for the project node
    def __init__(self, project_name, class_names):
        self.project_name = project_name
        self.class_list = []
        self.class_numbers = 0
        for i in range(len(class_names)):
            self.class_list.append(ClassTreeNode(class_names[i], self))
            self.class_numbers = self.class_numbers + 1;

    # Adds a class to the project node
    def add_class_node(self, class_name, method_names=None, structures_list=None):
        self.class_list.append(ClassTreeNode(class_name, self, method_names, structures_list))


# Class node used for each individual java class
class ClassTreeNode:

    # Constructor for the class node, will add in methods if provided, also holds any dependencies for the class if
    # provided
    def __init__(self, class_name, project_node, method_names=None, structures_list=None, dependencies_list=None):
        self.class_name = class_name
        self.project_node = project_node
        self.method_node_list = []
        self.dependencies_list = dependencies_list
        if method_names is not None:
            for i in range(len(method_names)):
                self.method_node_list.append(MethodTreeNode(method_names[i], self, structures_list))

    # Adds another method to the class, will add in structures too if not null
    def add_method_node(self, method_names, structures_list=None):
        if self.method_node_list is None:
            self.method_node_list = []
            self.method_node_list.append(MethodTreeNode(method_names, self))
        else:
            self.method_node_list.append(MethodTreeNode(method_names, self))

    # Adds in dependencies to the class if needed
    def add_dependency(self, dependency_name, project_node, method_names, structures_list):
        if self.dependencies_list is None:
            self.dependencies_list = []
            self.dependencies_list.append(ClassTreeNode(dependency_name, project_node, method_names, structures_list))
        else:
            self.dependencies_list.append(ClassTreeNode(dependency_name, project_node, method_names, structures_list))


# Method node class that holds information about each method
class MethodTreeNode:

    # Constructor for the method node class, will add in structures if provided
    def __init__(self, method_name, class_node, structures_list=None):
        self.method_name = method_name
        self.class_node = class_node
        self.structures_nodes = []
        if structures_list is not None:
            for i in range(len(structures_list)):
                self.structures_nodes.append(StructureTreeNode(structures_list[i], self))

    # Adds a structure node to the list
    def add_structure_node(self, structure_name):
        if self.structures_nodes is None:
            self.structures_nodes = []
            self.structures_nodes.append(StructureTreeNode(structure_name, self))
        else:
            self.structures_nodes.append(StructureTreeNode(structure_name, self))


# Structure node class can also hold an instance of itself if the structure is nested
class StructureTreeNode:

    # Constructor for the Structure node cladd, will add inner structures if provided
    def __init__(self, structure_name, method_node, inner_structures=None):
        self.structure_name = structure_name
        self.method_node = method_node
        if inner_structures is not None:
            for i in range(len(inner_structures)):
                self.inner_structures = []
                self.inner_structures.append(StructureTreeNode(inner_structures[i], self.method_node))

    # Adds an inner structure to the list
    def add_inner_structure(self, inner_structure_name):
        if self.inner_structures is None:
            self.inner_structures = []
            self.inner_structures.append(StructureTreeNode(inner_structure_name, self.method_node))
        else:
            self.inner_structures.append(StructureTreeNode(inner_structure_name, self.method_node))


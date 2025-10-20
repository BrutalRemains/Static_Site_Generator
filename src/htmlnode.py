class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        parts = [f' {k}="{v}"' for k, v in self.props.items()]
        return "".join(parts)
    
    def __repr__(self):
        child_count = 0 if self.children is None else len(self.children)
        return f"HTMLNode(tag={self.tag!r}, value={self.value}, children={child_count}, props={self.props!r})"
    
class LeafNode(HTMLNode):   
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        props_str = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):   
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag needed!")
        if self.children is None:
            raise ValueError("Children needed")
        
        html_str = f'<{self.tag}>'
        for child in self.children:
            child_to_html = child.to_html()
            html_str += child_to_html

        html_str += f'</{self.tag}>'
        return html_str
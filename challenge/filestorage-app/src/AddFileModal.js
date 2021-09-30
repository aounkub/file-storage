import React, {Component} from "react";
import {Modal, Button, Row, Col, Form} from "react-bootstrap";

export class AddFileModal extends Component{
    constructor(props){
        super(props);
        this.handleSubmit=this.handleSubmit.bind(this);
        this.handleFileSelected=this.handleFileSelected.bind(this);
        this.delete=this.delete.bind(this);
    }

    textfilename = "";
    filesrc = process.env.REACT_APP_FILEPATH+this.textfilename;

    handleSubmit(event){
        event.preventDefault();
        fetch(process.env.REACT_APP_API+'filestorage',{
            method:'POST',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                FilesName:this.textfilename,
            })
        })
        .then(res=>res.json())
        .then((result)=>{
            this.textfilename = "";
            alert(result);
        },
        (error)=>{
            alert('Failed');
        })
    }

    handleFileSelected(event){
        event.preventDefault();
        this.textfilename=event.target.files[0].name;
        const formData = new FormData();
        const files = event.target.files;
        for (let i = 0; i < files.length;i++){
            formData.append(
                `myFile_${i}`,
                files[i],
            );
        }
        fetch(process.env.REACT_APP_API+'filestorage/UploadFile',{
            method: "POST",
            body: formData
        })
        .then(res=>res.json())
        .then((result)=>{
            this.filesrc=process.env.REACT_APP_FILEPATH+result;
            this.textfilename=result;
        },
        (error)=>{
            alert('Failed');
        })
    }

    delete(event){
        event.preventDefault();
        const number = event.target.value;
        const name = this.textfilename[number];
        if(window.confirm('Do you want to delete '+name+' ?')){
            fetch(process.env.REACT_APP_API+'filestorage/DeleteFile',{
                method: "DELETE",
                body:JSON.stringify({
                    DeleteFileName: name,
                })
            })
            .then(res=>res.json()
            .then((result)=>{
                this.textfilename.splice(number,1);
                console.log(result);
            },
            (error)=>{
                alert("Filed To delete");
            }
            ))
        }
    }

    render(){
        return(
            <div className="container">

<Modal
{...this.props}
size="lg"
aria-labelledby="contained-modal-title-vcenter"
centered
>
    <Modal.Header>
        <Modal.Title id="contained-modal-title-vcenter">
            Upload File
        </Modal.Title>
    </Modal.Header>
    <Modal.Body>
        <Row>
            <Col>
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group >
                        <input onChange={this.handleFileSelected} type="File" multiple/>

                    </Form.Group>
                    <Form.Group controlId="FileName">
                        <Form.Label>File Name</Form.Label>
                            {Array.from(Array(this.textfilename.length)).map((c, number) => {
                                return(
                                    <><Row><Col xs={9}><Form.Control type="text" name="FileName"
                                        disabled
                                        value={this.textfilename[number]} />
                                        </Col><Col><Button variant="danger"
                                            type="reset"
                                            value={number}
                                            onClick={this.delete}
                                            >X</Button></Col></Row></>
                                );
                            })}
                    </Form.Group>
                        <Button variant="primary" type="submit" onClick={this.props.onHide}>
                            Upload
                        </Button>    
                </Form>
            </Col>
            
        </Row>
    </Modal.Body>

    <Modal.Footer>
        <Button variant="danger" onClick={this.props.onHide}>Close</Button>

    </Modal.Footer>

</Modal>

            </div>
        )
    }
}
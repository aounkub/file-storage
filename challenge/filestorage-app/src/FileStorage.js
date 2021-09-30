import React,{Component} from "react";
import { Table } from "react-bootstrap";

import {Button, ButtonToolbar} from "react-bootstrap";
import { AddFileModal } from "./AddFileModal";

export class FileStorage extends Component{

    constructor(probs){
        super(probs);
        this.state={files:[], addModalShow:false}
    }

    refreshList(){
        fetch(process.env.REACT_APP_API+"filestorage")
        .then(response=>response.json()
        .then(data=>{
            this.setState({files:data});
        }));
    }

    componentDidMount(){
        this.refreshList();
    }
    
    componentDidUpdate(){
        this.refreshList();
    }

    deleteFile(fileid, filename){
        if(window.confirm("Do yo want to delete "+filename+" ?")){
            fetch(process.env.REACT_APP_API+'filestorage/'+fileid,{
                method: "DELETE",
                headers:{
                    'Accept':'application/json',
                    'Content-Type':'application/json'
                },
            })
        }
    }

    
    render(){
        const {files}=this.state;

        let addModalClose=()=>this.setState({addModalShow:false});
        return(
            <div className="mt-5 d-flex justify-content-left">
                <Table className="mt-4" striped bordered hover size="sm">
                    <thead>
                        <tr>
                            <th>File Name</th>
                            <th>Upload Date</th>
                            <th>Options</th>
                        </tr>
                    </thead>
                    <tbody>
                        {files.map(file=>
                            <tr key={file.FileId}>
                                <td><a>{file.FileName}</a></td>
                                <td>{file.UpdateDate}</td>
                                <td>
<ButtonToolbar>
    <Button className="mr-2" variant="danger" 
    onClick={()=>this.deleteFile(file.FileId, file.FileName)}>
        Delete
    </Button>
</ButtonToolbar>
                                </td>
                            </tr>)}
                    </tbody>
                    <ButtonToolbar>
                        <Button variant='primary'
                        onClick={()=>this.setState({addModalShow:true})}>
                            Upload
                        </Button>

                        <AddFileModal show={this.state.addModalShow}
                        onHide={addModalClose}/>
                    </ButtonToolbar>
                </Table>

                
            </div>
        )

    }

}
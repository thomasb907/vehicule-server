import { VehicleStore } from '../store/vehicle';
import { Request, Response } from 'express';

interface Parameters {
  id: string;
}

export class DeleteVehicleController {
  constructor(private readonly vehicleStore: VehicleStore) {}


  public async handle(req: Request<Parameters>, res: Response): Promise<void> {
    try{
      const ID_string : string = req.params.id;
      const ID : number = parseInt(ID_string);
      await this.vehicleStore.deleteVehicle({id: ID});
      res.status(200).send("succes")
    }
    catch {
      res.status(500).send();
    }
  }
}


